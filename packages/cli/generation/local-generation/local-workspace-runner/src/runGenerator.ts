import { Audiences, generatorsYml } from "@fern-api/configuration";
import { runDocker } from "@fern-api/docker-utils";
import { AbsoluteFilePath, waitUntilPathExists } from "@fern-api/fs-utils";
import { generateIntermediateRepresentation } from "@fern-api/ir-generator";
import { HttpEndpoint, IntermediateRepresentation } from "@fern-api/ir-sdk";
import { TaskContext } from "@fern-api/task-context";
import { FernWorkspace } from "@fern-api/workspace-loader";
import { FernFiddle } from "@fern-fern/fiddle-sdk";
import { FernGeneratorCli } from "@fern-fern/generator-cli-sdk";
import * as FernGeneratorExecParsing from "@fern-fern/generator-exec-sdk/serialization";
import { writeFile } from "fs/promises";
import tmp, { DirectoryResult } from "tmp-promise";
import urlJoin from "url-join";
import { DOCKER_CODEGEN_OUTPUT_DIRECTORY, DOCKER_GENERATOR_CONFIG_PATH, DOCKER_PATH_TO_IR } from "./constants";
import { getGeneratorConfig } from "./getGeneratorConfig";
import { getIntermediateRepresentation } from "./getIntermediateRepresentation";
import { LocalTaskHandler } from "./LocalTaskHandler";

export interface GeneratorRunResponse {
    /* Path to the generated IR */
    absolutePathToIr: AbsoluteFilePath;
    /* Path to the generated config.json */
    absolutePathToConfigJson: AbsoluteFilePath;
}

export async function writeFilesToDiskAndRunGenerator({
    organization,
    workspace,
    generatorInvocation,
    absolutePathToLocalOutput,
    absolutePathToLocalSnippetJSON,
    absolutePathToLocalSnippetTemplateJSON,
    absolutePathToFernConfig,
    audiences,
    workspaceTempDir,
    keepDocker,
    context,
    irVersionOverride,
    outputVersionOverride,
    writeUnitTests,
    generateOauthClients,
    generatePaginatedClients
}: {
    organization: string;
    workspace: FernWorkspace;
    generatorInvocation: generatorsYml.GeneratorInvocation;
    absolutePathToLocalOutput: AbsoluteFilePath;
    absolutePathToLocalSnippetJSON: AbsoluteFilePath | undefined;
    absolutePathToLocalSnippetTemplateJSON: AbsoluteFilePath | undefined;
    absolutePathToFernConfig: AbsoluteFilePath | undefined;
    audiences: Audiences;
    workspaceTempDir: DirectoryResult;
    keepDocker: boolean;
    context: TaskContext;
    irVersionOverride: string | undefined;
    outputVersionOverride: string | undefined;
    writeUnitTests: boolean;
    generateOauthClients: boolean;
    generatePaginatedClients: boolean;
}): Promise<GeneratorRunResponse> {
    const absolutePathToIr = await writeIrToFile({
        workspace,
        audiences,
        generatorInvocation,
        workspaceTempDir,
        context,
        irVersionOverride
    });
    context.logger.debug("Wrote IR to: " + absolutePathToIr);

    const configJsonFile = await tmp.file({
        tmpdir: workspaceTempDir.path
    });
    const absolutePathToWriteConfigJson = AbsoluteFilePath.of(configJsonFile.path);
    context.logger.debug("Will write config.json to: " + absolutePathToWriteConfigJson);

    const tmpOutputDirectory = await tmp.dir({
        tmpdir: workspaceTempDir.path
    });
    const absolutePathToTmpOutputDirectory = AbsoluteFilePath.of(tmpOutputDirectory.path);
    context.logger.debug("Will write output to: " + absolutePathToTmpOutputDirectory);

    let absolutePathToTmpSnippetJSON = undefined;
    if (absolutePathToLocalSnippetJSON != null) {
        const snippetJsonFile = await tmp.file({
            tmpdir: workspaceTempDir.path
        });
        absolutePathToTmpSnippetJSON = AbsoluteFilePath.of(snippetJsonFile.path);
        context.logger.debug("Will write snippet.json to: " + absolutePathToTmpSnippetJSON);
    }

    let absolutePathToTmpSnippetTemplatesJSON = undefined;
    if (absolutePathToLocalSnippetTemplateJSON != null) {
        const snippetTemplatesJsonFile = await tmp.file({
            tmpdir: workspaceTempDir.path
        });
        absolutePathToTmpSnippetTemplatesJSON = AbsoluteFilePath.of(snippetTemplatesJsonFile.path);
        context.logger.debug("Will write snippet-templates.json to: " + absolutePathToTmpSnippetTemplatesJSON);
    }

    let absolutePathToTmpFeaturesYml = undefined;
    if (absolutePathToLocalSnippetJSON != null) {
        // We only write the README.md when snippets are available.
        const feautresYmlFile = await tmp.file({
            tmpdir: workspaceTempDir.path
        });
        absolutePathToTmpFeaturesYml = AbsoluteFilePath.of(feautresYmlFile.path);
        context.logger.debug("Will write features.yml to: " + absolutePathToTmpFeaturesYml);
    }

    const absolutePathToTmpReadmeConfig = await writeReadmeConfig({
        workspace,
        organization,
        outputVersionOverride,
        audiences,
        generatorInvocation,
        workspaceTempDir,
        context
    });

    await runGenerator({
        absolutePathToOutput: absolutePathToTmpOutputDirectory,
        absolutePathToSnippet: absolutePathToTmpSnippetJSON,
        absolutePathToSnippetTemplates: absolutePathToTmpSnippetTemplatesJSON,
        absolutePathToFeaturesYml: absolutePathToTmpFeaturesYml,
        absolutePathToIr,
        absolutePathToWriteConfigJson,
        workspaceName: workspace.name,
        organization,
        outputVersion: outputVersionOverride,
        keepDocker,
        generatorInvocation,
        context,
        writeUnitTests,
        generateOauthClients,
        generatePaginatedClients
    });

    const taskHandler = new LocalTaskHandler({
        context,
        absolutePathToLocalOutput,
        absolutePathToTmpOutputDirectory,
        absolutePathToLocalSnippetJSON,
        absolutePathToLocalSnippetTemplateJSON,
        absolutePathToTmpFeaturesYml,
        absolutePathToTmpReadmeConfig,
        absolutePathToTmpSnippetJSON,
        absolutePathToTmpSnippetTemplatesJSON
    });

    await taskHandler.copyGeneratedFiles();

    return {
        absolutePathToIr,
        absolutePathToConfigJson: absolutePathToWriteConfigJson
    };
}

async function writeReadmeConfig({
    workspace,
    organization,
    outputVersionOverride,
    audiences,
    generatorInvocation,
    workspaceTempDir,
    context
}: {
    workspace: FernWorkspace;
    organization: string;
    outputVersionOverride: string | undefined;
    audiences: Audiences;
    generatorInvocation: generatorsYml.GeneratorInvocation;
    workspaceTempDir: DirectoryResult;
    context: TaskContext;
}): Promise<AbsoluteFilePath> {
    // We can't use the IR used by the generator beacause it's shape is unknown.
    //
    // Although duplicative, we'll generate the IR again and use it to find the
    // endpoint IDs referenced by the user-defined generator configuration.
    const intermediateRepresentation = await generateIntermediateRepresentation({
        workspace,
        audiences,
        generationLanguage: generatorInvocation.language,
        smartCasing: generatorInvocation.smartCasing,
        disableExamples: generatorInvocation.disableExamples
    });

    const readmeConfig = await generateReadmeConfig({
        organization,
        outputVersionOverride,
        intermediateRepresentation,
        generatorInvocation,
        context
    });

    const readmeConfigFile = await tmp.file({
        tmpdir: workspaceTempDir.path
    });
    const absolutePathToReadmeConfig = AbsoluteFilePath.of(readmeConfigFile.path);
    await writeFile(absolutePathToReadmeConfig, JSON.stringify(readmeConfig, undefined, 4));
    context.logger.debug(`Wrote readme configuration to ${absolutePathToReadmeConfig}`);
    return absolutePathToReadmeConfig;
}

async function generateReadmeConfig({
    organization,
    outputVersionOverride,
    intermediateRepresentation,
    generatorInvocation,
    context
}: {
    organization: string;
    outputVersionOverride: string | undefined;
    intermediateRepresentation: IntermediateRepresentation;
    generatorInvocation: generatorsYml.GeneratorInvocation;
    context: TaskContext;
}): Promise<FernGeneratorCli.ReadmeConfig> {
    return {
        organization,
        language: generatorInvocation.language ?? "",
        bannerLink: generatorInvocation.readme?.bannerLink,
        docsLink: generatorInvocation.readme?.docsLink,
        publishInfo: await getReadmePublishInfo({
            outputVersionOverride,
            generatorInvocation
        }),
        featureEndpoints: await resolveFeatureEndpoints({
            intermediateRepresentation,
            generatorInvocation
        })
    };
}

// TODO: This is terribly inefficient. Refactor this.
async function resolveFeatureEndpoints({
    intermediateRepresentation,
    generatorInvocation
}: {
    intermediateRepresentation: IntermediateRepresentation;
    generatorInvocation: generatorsYml.GeneratorInvocation;
}): Promise<Record<FernGeneratorCli.FeatureId, FernGeneratorCli.EndpointId[]>> {
    const featureEndpoints: Record<FernGeneratorCli.FeatureId, FernGeneratorCli.EndpointId[]> = {};
    for (const [featureId, endpoints] of Object.entries(generatorInvocation.readme?.features ?? {})) {
        const endpointObjects = endpoints.map((endpoint) => getReadmeEndpointObject({ endpoint }));
        const endpointIds: FernGeneratorCli.EndpointId[] = [];
        let found = false;
        for (const endpointObject of endpointObjects) {
            for (const service of Object.values(intermediateRepresentation.services)) {
                if (found) {
                    break;
                }
                for (const endpoint of service.endpoints) {
                    if (
                        matchEndpointObjectToEndpoint({
                            endpointObject,
                            endpoint
                        })
                    ) {
                        endpointIds.push(FernGeneratorCli.EndpointId(endpoint.id));
                        found = true;
                        break;
                    }
                }
            }
            if (!found) {
                throw new Error(
                    `Could not find endpoint with method ${endpointObject.method} and path ${endpointObject.path}`
                );
            }
            found = false;
        }
        featureEndpoints[FernGeneratorCli.FeatureId(featureId)] = endpointIds;
    }
    return featureEndpoints;
}

function matchEndpointObjectToEndpoint({
    endpointObject,
    endpoint
}: {
    endpointObject: generatorsYml.ReadmeFeatureObjectSchema;
    endpoint: HttpEndpoint;
}): boolean {
    return (
        endpointObject.method === endpoint.method &&
        getFullPathForEndpoint(endpoint) === endpointObject.path &&
        (!endpointObject.stream || endpoint.response?.body?.type === "streaming")
    );
}

async function getReadmePublishInfo({
    outputVersionOverride,
    generatorInvocation
}: {
    outputVersionOverride: string | undefined;
    generatorInvocation: generatorsYml.GeneratorInvocation;
}): Promise<FernGeneratorCli.PublishInfo | undefined> {
    switch (generatorInvocation.outputMode.type) {
        case "github":
            return getReadmePublishInfoForGithub({
                outputVersionOverride,
                language: generatorInvocation.language,
                outputMode: generatorInvocation.outputMode
            });
        case "githubV2":
            return getReadmePublishInfoForGithub({
                outputVersionOverride,
                language: generatorInvocation.language,
                outputMode: generatorInvocation.outputMode.githubV2
            });
    }
    return undefined;
}

async function getReadmePublishInfoForGithub({
    outputVersionOverride,
    language,
    outputMode
}: {
    outputVersionOverride: string | undefined;
    language: generatorsYml.GenerationLanguage | undefined;
    outputMode: FernFiddle.GithubOutputMode;
}): Promise<FernGeneratorCli.PublishInfo | undefined> {
    if (language === "go") {
        return FernGeneratorCli.PublishInfo.go({
            owner: outputMode.owner,
            repo: outputMode.repo,
            version: outputVersionOverride ?? "0.0.1"
        });
    }
    return undefined;
}

function getReadmeEndpointObject({
    endpoint
}: {
    endpoint: generatorsYml.ReadmeFeatureSchema;
}): generatorsYml.ReadmeFeatureObjectSchema {
    if (typeof endpoint === "string") {
        const split = endpoint.split(" ");
        if (split.length !== 2 || split[0] == null || split[1] == null) {
            throw new Error(`Invalid endpoint string: ${endpoint}`);
        }
        return {
            method: split[0],
            path: split[1]
        };
    }
    return endpoint;
}

// TODO: Move this to the IR.
function getFullPathForEndpoint(endpoint: HttpEndpoint): string {
    let url = "";
    if (endpoint.fullPath.head.length > 0) {
        url = urlJoin(url, endpoint.fullPath.head);
    }
    for (const part of endpoint.fullPath.parts) {
        url = urlJoin(url, "{" + part.pathParameter + "}");
        if (part.tail.length > 0) {
            url = urlJoin(url, part.tail);
        }
    }
    return url.startsWith("/") ? url : `/${url}`;
}

async function writeIrToFile({
    workspace,
    audiences,
    generatorInvocation,
    workspaceTempDir,
    context,
    irVersionOverride
}: {
    workspace: FernWorkspace;
    audiences: Audiences;
    generatorInvocation: generatorsYml.GeneratorInvocation;
    workspaceTempDir: DirectoryResult;
    context: TaskContext;
    irVersionOverride: string | undefined;
}): Promise<AbsoluteFilePath> {
    const intermediateRepresentation = await getIntermediateRepresentation({
        workspace,
        audiences,
        generatorInvocation,
        context,
        irVersionOverride
    });
    context.logger.debug("Migrated IR");
    const irFile = await tmp.file({
        tmpdir: workspaceTempDir.path
    });
    const absolutePathToIr = AbsoluteFilePath.of(irFile.path);
    await writeFile(absolutePathToIr, JSON.stringify(intermediateRepresentation, undefined, 4));
    context.logger.debug(`Wrote IR to ${absolutePathToIr}`);
    return absolutePathToIr;
}

export declare namespace runGenerator {
    export interface Args {
        workspaceName: string;
        organization: string;
        outputVersion?: string | undefined;

        absolutePathToIr: AbsoluteFilePath;
        absolutePathToOutput: AbsoluteFilePath;
        absolutePathToSnippet: AbsoluteFilePath | undefined;
        absolutePathToSnippetTemplates: AbsoluteFilePath | undefined;
        absolutePathToFeaturesYml: AbsoluteFilePath | undefined;
        absolutePathToWriteConfigJson: AbsoluteFilePath;
        keepDocker: boolean;
        context: TaskContext;
        generatorInvocation: generatorsYml.GeneratorInvocation;
        writeUnitTests: boolean;
        generateOauthClients: boolean;
        generatePaginatedClients: boolean;
    }

    export interface Result {
        featuresYml: string | undefined;
    }
}

export async function runGenerator({
    workspaceName,
    organization,
    outputVersion,
    absolutePathToOutput,
    absolutePathToSnippet,
    absolutePathToSnippetTemplates,
    absolutePathToIr,
    absolutePathToFeaturesYml,
    absolutePathToWriteConfigJson,
    keepDocker,
    generatorInvocation,
    writeUnitTests,
    generateOauthClients,
    generatePaginatedClients
}: runGenerator.Args): Promise<void> {
    const { name, version, config: customConfig } = generatorInvocation;
    const imageName = `${name}:${version}`;

    const binds = [
        `${absolutePathToWriteConfigJson}:${DOCKER_GENERATOR_CONFIG_PATH}:ro`,
        `${absolutePathToIr}:${DOCKER_PATH_TO_IR}:ro`,
        `${absolutePathToOutput}:${DOCKER_CODEGEN_OUTPUT_DIRECTORY}`
    ];
    const { config, binds: bindsForGenerators } = getGeneratorConfig({
        generatorInvocation,
        customConfig,
        workspaceName,
        outputVersion,
        organization,
        absolutePathToSnippet,
        absolutePathToSnippetTemplates,
        absolutePathToFeaturesYml,
        writeUnitTests,
        generateOauthClients,
        generatePaginatedClients
    });
    binds.push(...bindsForGenerators);

    const parsedConfig = await FernGeneratorExecParsing.GeneratorConfig.json(config);
    if (!parsedConfig.ok) {
        throw new Error(`Failed to parse config.json into ${absolutePathToWriteConfigJson}`);
    }

    await writeFile(absolutePathToWriteConfigJson, JSON.stringify(parsedConfig.value, undefined, 4));

    const doesConfigJsonExist = await waitUntilPathExists(absolutePathToWriteConfigJson, 5_000);
    if (!doesConfigJsonExist) {
        throw new Error(`Failed to create ${absolutePathToWriteConfigJson}`);
    }

    await runDocker({
        imageName,
        args: [DOCKER_GENERATOR_CONFIG_PATH],
        binds,
        removeAfterCompletion: !keepDocker
    });
}
