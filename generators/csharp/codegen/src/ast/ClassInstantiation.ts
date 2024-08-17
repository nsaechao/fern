import { Arguments, isNamedArgument, NamedArgument, UnnamedArgument } from "./Argument";
import { ClassReference } from "./ClassReference";
import { AstNode } from "./core/AstNode";
import { Writer } from "./core/Writer";

export declare namespace ClassInstantiation {
    interface Args {
        classReference: ClassReference;
        // A map of the field for the class and the value to be assigned to it.
        arguments_: Arguments;
        // Includes the class reference's namespace, even if it's not always needed.
        includeNamespace?: boolean;
    }
}

export class ClassInstantiation extends AstNode {
    public readonly classReference: ClassReference;
    public readonly arguments_: NamedArgument[] | UnnamedArgument[];
    public readonly includeNamespace: boolean;

    constructor({ classReference, arguments_, includeNamespace }: ClassInstantiation.Args) {
        super();
        this.classReference = classReference;
        this.arguments_ = arguments_;
        this.includeNamespace = includeNamespace ?? false;
    }

    public write(writer: Writer): void {
        const hasNamedArguments =
            this.arguments_.length > 0 && this.arguments_[0] != null && isNamedArgument(this.arguments_[0]);

        const name = this.includeNamespace
            ? `${this.classReference.namespace}.${this.classReference.name}`
            : this.classReference.name;

        writer.write(`new ${name}`);

        if (hasNamedArguments) {
            writer.write("{ ");
        } else {
            writer.write("(");
        }

        writer.newLine();
        writer.indent();
        this.arguments_.forEach((argument, idx) => {
            if (isNamedArgument(argument)) {
                writer.write(`${argument.name} = `);
                argument.assignment.write(writer);
            } else {
                argument.write(writer);
            }
            if (idx < this.arguments_.length - 1) {
                writer.write(", ");
            }
        });
        writer.writeLine();
        writer.dedent();

        if (hasNamedArguments) {
            writer.write("}");
        } else {
            writer.write(")");
        }
    }
}
