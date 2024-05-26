import { FERNIGNORE_FILENAME, README_FILENAME } from "@fern-api/configuration";
import { AbsoluteFilePath, doesPathExist, join, RelativeFilePath } from "@fern-api/fs-utils";
import { loggingExeca } from "@fern-api/logging-execa";
import { TaskContext } from "@fern-api/task-context";
import decompress from "decompress";
import { cp, readdir, readFile, rm, rmdir } from "fs/promises";
import tmp from "tmp-promise";

export declare namespace LocalTaskHandler {
    export interface Init {
        context: TaskContext;
        absolutePathToTmpOutputDirectory: AbsoluteFilePath;
        absolutePathToTmpSnippetJSON: AbsoluteFilePath | undefined;
        absolutePathToLocalSnippetTemplateJSON: AbsoluteFilePath | undefined;
        absolutePathToTmpFeaturesYml: AbsoluteFilePath | undefined;
        absolutePathToLocalOutput: AbsoluteFilePath;
        absolutePathToLocalSnippetJSON: AbsoluteFilePath | undefined;
        absolutePathToTmpSnippetTemplatesJSON: AbsoluteFilePath | undefined;
    }
}

export class LocalTaskHandler {
    private context: TaskContext;
    private absolutePathToTmpOutputDirectory: AbsoluteFilePath;
    private absolutePathToTmpSnippetJSON: AbsoluteFilePath | undefined;
    private absolutePathToTmpSnippetTemplatesJSON: AbsoluteFilePath | undefined;
    private absolutePathToTmpFeaturesYml: AbsoluteFilePath | undefined;
    private absolutePathToLocalSnippetTemplateJSON: AbsoluteFilePath | undefined;
    private absolutePathToLocalOutput: AbsoluteFilePath;
    private absolutePathToLocalSnippetJSON: AbsoluteFilePath | undefined;

    constructor({
        context,
        absolutePathToTmpOutputDirectory,
        absolutePathToTmpSnippetJSON,
        absolutePathToLocalSnippetTemplateJSON,
        absolutePathToLocalOutput,
        absolutePathToLocalSnippetJSON,
        absolutePathToTmpSnippetTemplatesJSON,
        absolutePathToTmpFeaturesYml
    }: LocalTaskHandler.Init) {
        this.context = context;
        this.absolutePathToLocalOutput = absolutePathToLocalOutput;
        this.absolutePathToTmpOutputDirectory = absolutePathToTmpOutputDirectory;
        this.absolutePathToTmpSnippetJSON = absolutePathToTmpSnippetJSON;
        this.absolutePathToLocalSnippetJSON = absolutePathToLocalSnippetJSON;
        this.absolutePathToLocalSnippetTemplateJSON = absolutePathToLocalSnippetTemplateJSON;
        this.absolutePathToTmpSnippetTemplatesJSON = absolutePathToTmpSnippetTemplatesJSON;
        this.absolutePathToTmpFeaturesYml = absolutePathToTmpFeaturesYml;
    }

    public async copyGeneratedFiles(): Promise<void> {
        if (await this.isFernIgnorePresent()) {
            await this.copyGeneratedFilesWithFernIgnore();
        } else {
            await this.copyGeneratedFilesNoFernIgnore();
        }
        if (
            this.absolutePathToTmpSnippetJSON != null &&
            this.absolutePathToLocalSnippetJSON != null &&
            (await doesPathExist(this.absolutePathToTmpSnippetJSON))
        ) {
            await this.copySnippetJSON({
                absolutePathToTmpSnippetJSON: this.absolutePathToTmpSnippetJSON,
                absolutePathToLocalSnippetJSON: this.absolutePathToLocalSnippetJSON
            });
        }

        if (
            this.absolutePathToTmpSnippetTemplatesJSON != null &&
            this.absolutePathToLocalSnippetTemplateJSON != null &&
            (await doesPathExist(this.absolutePathToTmpSnippetTemplatesJSON))
        ) {
            await this.copySnippetJSON({
                absolutePathToTmpSnippetJSON: this.absolutePathToTmpSnippetTemplatesJSON,
                absolutePathToLocalSnippetJSON: this.absolutePathToLocalSnippetTemplateJSON
            });
        }

        // TODO: This is where we should copy out the features.yml, and generate the README.md.
        if (this.absolutePathToTmpFeaturesYml != null) {
            // TODO: Read the features.yml as JSON.
            // TODO: Call the generator-cli with the features.yml, snippet.json and readme config.
            const absolutePathToReadme = AbsoluteFilePath.of(
                join(this.absolutePathToLocalOutput, RelativeFilePath.of(README_FILENAME))
            );
            const { stdout } = await execa(
                "node",
                [
                    "~/code/",
                    "generate readme",
                    "--readme-config",
                    // TODO: Parse this value and pass it in here.
                    "~/code/fern/fern-platform/packages/generator-cli/src/__test__/fixtures/cohere-go/readme.json",
                    "--feature-config",
                    this.absolutePathToTmpFeaturesYml,
                    "--snippets",
                    this.absolutePathToTmpSnippetJSON,
                    "--output",
                    absolutePathToReadme
                ],
                {
                    reject: false
                }
            );
        }
    }

    private async isFernIgnorePresent(): Promise<boolean> {
        const absolutePathToFernignore = AbsoluteFilePath.of(
            join(this.absolutePathToLocalOutput, RelativeFilePath.of(FERNIGNORE_FILENAME))
        );
        return await doesPathExist(absolutePathToFernignore);
    }

    private async copyGeneratedFilesWithFernIgnore(): Promise<void> {
        // Create temp directory to resolve .fernignore
        const tmpOutputResolutionDir = AbsoluteFilePath.of((await tmp.dir({})).path);

        // Read all .fernignore paths
        const absolutePathToFernignore = AbsoluteFilePath.of(
            join(this.absolutePathToLocalOutput, RelativeFilePath.of(FERNIGNORE_FILENAME))
        );
        const fernIngnorePaths = await getFernIgnorePaths({ absolutePathToFernignore });

        // Copy files from local output to tmp directory
        await cp(this.absolutePathToLocalOutput, tmpOutputResolutionDir, { recursive: true });

        // In tmp directory initialize a `.git` directory
        await this.runGitCommand(["init"], tmpOutputResolutionDir);
        await this.runGitCommand(["add", "."], tmpOutputResolutionDir);

        const response = await this.runGitCommand(["config", "--list"], tmpOutputResolutionDir);
        if (!response.includes("user.name")) {
            await this.runGitCommand(["config", "user.name", "fern-api"], tmpOutputResolutionDir);
            await this.runGitCommand(["config", "user.email", "info@buildwithfern.com"], tmpOutputResolutionDir);
        }
        await this.runGitCommand(["commit", "--allow-empty", "-m", '"init"'], tmpOutputResolutionDir);

        // Stage deletions `git rm -rf .`
        await this.runGitCommand(["rm", "-rf", "."], tmpOutputResolutionDir);

        // Copy all files from generated temp dir
        await this.copyGeneratedFilesToDirectory(tmpOutputResolutionDir);

        // Undo changes to fernignore paths
        await this.runGitCommand(["reset", "--", ...fernIngnorePaths], tmpOutputResolutionDir);
        await this.runGitCommand(["restore", "."], tmpOutputResolutionDir);

        // Delete local output directory and copy all files from the generated directory
        await rmdir(this.absolutePathToLocalOutput, { recursive: true });
        await cp(tmpOutputResolutionDir, this.absolutePathToLocalOutput, { recursive: true });
    }

    /**
     * If no `.fernignore` is present we can delete the local output directory entirely and
     * copy the generated output from the tmp directory.
     */
    private async copyGeneratedFilesNoFernIgnore(): Promise<void> {
        this.context.logger.debug(`rm -rf ${this.absolutePathToLocalOutput}`);
        await rm(this.absolutePathToLocalOutput, { force: true, recursive: true });
        await this.copyGeneratedFilesToDirectory(this.absolutePathToLocalOutput);
    }

    private async copyGeneratedFilesToDirectory(outputPath: AbsoluteFilePath): Promise<void> {
        const [firstLocalOutputItem, ...remaininglocalOutputItems] = await readdir(
            this.absolutePathToTmpOutputDirectory
        );
        if (firstLocalOutputItem == null) {
            return;
        }
        this.context.logger.debug(`Copying generated files to ${outputPath}`);
        if (firstLocalOutputItem.endsWith(".zip")) {
            await decompress(
                join(this.absolutePathToTmpOutputDirectory, RelativeFilePath.of(firstLocalOutputItem)),
                outputPath
            );
            for (const localOutputItem of remaininglocalOutputItems) {
                await cp(
                    join(this.absolutePathToTmpOutputDirectory, RelativeFilePath.of(localOutputItem)),
                    join(outputPath, RelativeFilePath.of(localOutputItem)),
                    { recursive: true }
                );
            }
        } else {
            await cp(this.absolutePathToTmpOutputDirectory, outputPath, { recursive: true });
        }
    }

    private async copySnippetJSON({
        absolutePathToTmpSnippetJSON,
        absolutePathToLocalSnippetJSON
    }: {
        absolutePathToTmpSnippetJSON: AbsoluteFilePath;
        absolutePathToLocalSnippetJSON: AbsoluteFilePath;
    }): Promise<void> {
        this.context.logger.debug(`Copying generated snippets to ${absolutePathToLocalSnippetJSON}`);
        await cp(absolutePathToTmpSnippetJSON, absolutePathToLocalSnippetJSON);
    }

    private async runGitCommand(options: string[], cwd: AbsoluteFilePath): Promise<string> {
        const response = await loggingExeca(this.context.logger, "git", options, {
            cwd,
            doNotPipeOutput: true
        });
        return response.stdout;
    }
}

const NEW_LINE_REGEX = /\r?\n/;

async function getFernIgnorePaths({
    absolutePathToFernignore
}: {
    absolutePathToFernignore: AbsoluteFilePath;
}): Promise<string[]> {
    const fernIgnoreFileContents = (await readFile(absolutePathToFernignore)).toString();
    return [
        FERNIGNORE_FILENAME,
        ...fernIgnoreFileContents
            .trim()
            .split(NEW_LINE_REGEX)
            .filter((line) => !line.startsWith("#") && line.length > 0)
    ];
}
