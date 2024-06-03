import { DEFINITION_DIRECTORY } from "@fern-api/configuration";
import { AbsoluteFilePath, join, RelativeFilePath } from "@fern-api/fs-utils";
import { LogLevel } from "@fern-api/logger";
import tmp from "tmp-promise";
import { GeneratorWorkspace } from "../../loadGeneratorWorkspaces";
import { Semaphore } from "../../Semaphore";
import { convertGeneratorWorkspaceToFernWorkspace } from "../../utils/convertSeedWorkspaceToFernWorkspace";
import { ScriptRunner } from "../test/ScriptRunner";
import { TaskContextFactory } from "../test/TaskContextFactory";
import { DockerTestRunner } from "../test/test-runner";
import { writeDotMock } from "../test/test-runner/TestRunner";

export async function runWithCustomFixture({
    pathToFixture,
    workspace,
    logLevel
}: {
    pathToFixture: AbsoluteFilePath;
    workspace: GeneratorWorkspace;
    logLevel: LogLevel;
}): Promise<void> {
    const lock = new Semaphore(1);
    const outputDir = await tmp.dir();
    const absolutePathToOutput = AbsoluteFilePath.of(outputDir.path);
    const taskContextFactory = new TaskContextFactory(logLevel);
    const customFixtureConfig = workspace.workspaceConfig.customFixtureConfig;

    const taskContext = taskContextFactory.create(
        `${workspace.workspaceName}:${"custom"} - ${customFixtureConfig?.outputFolder ?? ""}`
    );

    const dockerGeneratorRunner = new DockerTestRunner({
        generator: workspace,
        lock,
        taskContextFactory,
        skipScripts: true,
        keepDocker: true,
        scriptRunner: new ScriptRunner(workspace)
    });

    const fernWorkspace = await convertGeneratorWorkspaceToFernWorkspace({
        absolutePathToAPIDefinition: pathToFixture,
        taskContext,
        fixture: "custom",
        sdkLanguage: workspace.workspaceConfig.language
    });
    if (fernWorkspace == null) {
        taskContext.logger.error("Failed to load API definition.");
        return;
    }

    try {
        await dockerGeneratorRunner.build();
        await dockerGeneratorRunner.runGenerator({
            fernWorkspace,
            absolutePathToFernDefinition: join(pathToFixture, RelativeFilePath.of(DEFINITION_DIRECTORY)),
            absolutePathToWorkspace: pathToFixture,
            irVersion: workspace.workspaceConfig.irVersion,
            outputVersion: customFixtureConfig?.outputVersion,
            language: workspace.workspaceConfig.language,
            fixture: "custom",
            customConfig: customFixtureConfig?.customConfig,
            publishConfig: customFixtureConfig?.publishConfig,
            publishMetadata: customFixtureConfig?.publishMetadata,
            selectAudiences: customFixtureConfig?.audiences,
            taskContext,
            outputDir: absolutePathToOutput,
            outputMode: customFixtureConfig?.outputMode ?? workspace.workspaceConfig.defaultOutputMode,
            outputFolder: customFixtureConfig?.outputFolder ?? "custom",
            id: "custom",
            keepDocker: true
        });
        await writeDotMock({
            absolutePathToDotMockDirectory: absolutePathToOutput,
            absolutePathToFernDefinition: pathToFixture
        });
        taskContext.logger.info(`Wrote files to ${absolutePathToOutput}`);
    } catch (error) {
        taskContext.logger.error(`Encountered error while running generator. ${(error as Error)?.message}`);
    }
}
