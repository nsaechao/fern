import { MethodInvocation } from "../MethodInvocation";
import { Writer } from "../core/Writer";
import { python } from "../..";

describe("MethodInvocation", () => {
    let writer: Writer;

    beforeEach(() => {
        writer = new Writer();
    });

    it("should write a method invocation with no args", async () => {
        const invocation = python.invokeMethod({
            methodReference: python.reference({ name: "test_method" }),
            arguments_: []
        });

        const writer = new Writer();
        invocation.write(writer);

        expect(await writer.toStringFormatted()).toMatchSnapshot();
    });

    it("should write a method invocation with one positional arg", async () => {
        const invocation = python.invokeMethod({
            methodReference: python.reference({ name: "test_method" }),
            arguments_: [python.methodArgument({ value: python.codeBlock("42") })]
        });

        const writer = new Writer();
        invocation.write(writer);

        expect(await writer.toStringFormatted()).toMatchSnapshot();
    });

    it("should write a method invocation with one positional arg and one kwarg", async () => {
        const invocation = python.invokeMethod({
            methodReference: python.reference({ name: "test_method" }),
            arguments_: [
                python.methodArgument({ value: python.codeBlock("42") }),
                python.methodArgument({ name: "key", value: python.codeBlock("'value'") })
            ]
        });

        const writer = new Writer();
        invocation.write(writer);

        expect(await writer.toStringFormatted()).toMatchSnapshot();
    });

    it("should write a method invocation with multiple positional and kwarg args", async () => {
        const invocation = python.invokeMethod({
            methodReference: python.reference({ name: "test_method" }),
            arguments_: [
                python.methodArgument({ value: python.codeBlock("42") }),
                python.methodArgument({ value: python.codeBlock("'hello'") }),
                python.methodArgument({ name: "key1", value: python.codeBlock("True") }),
                python.methodArgument({ name: "key2", value: python.codeBlock("[1, 2, 3]") })
            ]
        });

        const writer = new Writer();
        invocation.write(writer);

        expect(await writer.toStringFormatted()).toMatchSnapshot();
    });

    it("should write a method invocation with a parent", async () => {
        const invocation = python.invokeMethod({
            methodReference: python.reference({ name: "parent_object", attribute: ["test_method"] }),
            arguments_: [
                python.methodArgument({ value: python.codeBlock("'arg1'") }),
                python.methodArgument({ name: "kwarg", value: python.codeBlock("42") })
            ]
        });

        const writer = new Writer();
        invocation.write(writer);

        expect(await writer.toStringFormatted()).toMatchSnapshot();
    });
});
