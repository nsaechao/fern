import { AstNode, Writer } from "@fern-api/generator-commons";
import { INDENT_SIZE } from "../lang";
import { Func } from "./Func";

export declare namespace Class {
    interface Args {
        name: string,
        functions: Func[]
    }
}

export class Class extends AstNode {

    public readonly name: string;
    public readonly functions: Func[];

    constructor({ 
        name,
        functions,
    }: Class.Args) {
        super(INDENT_SIZE);
        this.name = name;
        this.functions = functions;
    }

    public write(writer: Writer): void {

        writer.write(`class ${this.name} {`);

        writer.newLine();

            writer.openIndent();

            this.functions.forEach(func => {
                writer.writeNode(func);
                writer.newLine();
            });

            writer.closeIndent();

        writer.write("}");


    }
}
