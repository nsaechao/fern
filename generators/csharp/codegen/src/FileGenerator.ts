import { AbstractCsharpGeneratorContext, BaseCsharpCustomConfigSchema } from "./cli";
import { GeneratedFile } from "./utils/File";

export abstract class FileGenerator<T extends GeneratedFile> {
    protected constructor(protected readonly context: AbstractCsharpGeneratorContext<BaseCsharpCustomConfigSchema>) {}

    public async generate(): Promise<File> {
        this.context.logger.debug(`Generating file ${this.getFilepath()}`);
        return await this.generateFile();
    }

    /**
     * Returns the path of the file to generate.
     */
    public abstract getFilepath(): string;

    /**
     * Actually generates the file.
     */
    protected abstract generateFile(): Promise<T>;
}
