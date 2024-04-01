import { CSharpFile, FileGenerator } from "@fern-api/csharp-codegen";

export class RootClientGenerator extends FileGenerator<CSharpFile> {
    public getFilepath(): string {
        throw new Error("Method not implemented.");
    }

    protected generateFile(): Promise<CSharpFile> {
        throw new Error("Method not implemented.");
    }
}
