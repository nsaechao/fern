import { Audiences } from "@fern-api/configuration";
import { createFdrService } from "@fern-api/core";
import { AbsoluteFilePath } from "@fern-api/fs-utils";
import { loggingExeca } from "@fern-api/logging-execa";
import { askToLogin } from "@fern-api/login";
import { Project } from "@fern-api/project-loader";
import { convertIrToFdrApi } from "@fern-api/register";
import { convertOpenApiWorkspaceToFernWorkspace } from "@fern-api/workspace-loader";
import { readFile } from "fs/promises";
import tmp from "tmp-promise";
import { CliContext } from "../../cli-context/CliContext";
import { generateIrForFernWorkspace } from "../generate-ir/generateIrForFernWorkspace";

export async function generateFdrApiDefinitionForWorkspaces({
    project,
    outputFilepath,
    repository,
    cliContext,
    audiences
}: {
    repository: string;
    project: Project;
    outputFilepath: AbsoluteFilePath;
    cliContext: CliContext;
    audiences: Audiences;
}): Promise<void> {
    await Promise.all(
        project.apiWorkspaces.map(async (workspace) => {
            const token = await cliContext.runTask(async (context) => {
                return askToLogin(context);
            });

            await cliContext.runTaskForWorkspace(workspace, async (context) => {
                const fernWorkspace =
                    workspace.type === "oss"
                        ? await convertOpenApiWorkspaceToFernWorkspace(workspace, context)
                        : workspace;

                const ir = await generateIrForFernWorkspace({
                    workspace: fernWorkspace,
                    context,
                    generationLanguage: undefined,
                    audiences,
                    smartCasing: false,
                    disableExamples: false
                });

                const apiDefinition = convertIrToFdrApi({
                    ir,
                    snippetsConfig: {}
                });

                const fdrService = createFdrService({
                    token: token.value
                });

                const response = await fdrService.api.v1.register.registerApiDefinition({
                    orgId: project.config.organization,
                    apiId: ir.apiName.originalName,
                    definition: apiDefinition
                });

                const tmpDir = await tmp.dir();
                await loggingExeca(cliContext.logger, "git", ["clone", repository, "--depth=1"], {
                    doNotPipeOutput: true,
                    cwd: tmpDir.path
                });
                await loggingExeca(
                    cliContext.logger,
                    "fern",
                    ["fdr", "fdr.json", "--api", workspace.workspaceName ?? "api"],
                    {
                        doNotPipeOutput: true,
                        cwd: tmpDir.path
                    }
                );
                const previousDefinition = JSON.parse((await readFile(`${tmpDir.path}/fdr.json`)).toString());
                const response = await fdrService.api.v1.register.registerApiDefinition({
                    orgId: project.config.organization,
                    apiId: ir.apiName.originalName,
                    definition: apiDefinition
                });
            });
        })
    );
}
