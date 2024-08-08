import { AbsoluteFilePath, join, RelativeFilePath } from "@fern-api/fs-utils";
import path from "path";
import { ProtobufFileInfo, ProtobufParser } from "../parsers/ProtobufParser";

const TEST_DEFINITIONS = AbsoluteFilePath.of(path.join(__dirname, "parsers/protobuf/test-definitions"));

describe("protobuf parser", () => {
    const parser = new ProtobufParser();

    it("empty", async () => {
        const expected: ProtobufFileInfo = {
            csharpNamespace: undefined,
            packageName: undefined,
            serviceName: undefined
        };
        const actual = await parser.parse({
            absoluteFilePath: join(TEST_DEFINITIONS, RelativeFilePath.of("empty.proto"))
        });
        expect(actual).toEqual(expected);
    });

    it("exhaustive", async () => {
        const expected: ProtobufFileInfo = {
            csharpNamespace: "User.V1",
            packageName: "user.v1",
            serviceName: "User"
        };
        const actual = await parser.parse({
            absoluteFilePath: join(TEST_DEFINITIONS, RelativeFilePath.of("exhaustive.proto"))
        });
        expect(actual).toEqual(expected);
    });

    it("option", async () => {
        const expected: ProtobufFileInfo = {
            csharpNamespace: "User.V1",
            packageName: undefined,
            serviceName: undefined
        };
        const actual = await parser.parse({
            absoluteFilePath: join(TEST_DEFINITIONS, RelativeFilePath.of("option.proto"))
        });
        expect(actual).toEqual(expected);
    });

    it("package", async () => {
        const expected: ProtobufFileInfo = {
            csharpNamespace: undefined,
            packageName: "user.v1",
            serviceName: undefined
        };
        const actual = await parser.parse({
            absoluteFilePath: join(TEST_DEFINITIONS, RelativeFilePath.of("package.proto"))
        });
        expect(actual).toEqual(expected);
    });

    it("service", async () => {
        const expected: ProtobufFileInfo = {
            csharpNamespace: undefined,
            packageName: undefined,
            serviceName: "User"
        };
        const actual = await parser.parse({
            absoluteFilePath: join(TEST_DEFINITIONS, RelativeFilePath.of("service.proto"))
        });
        expect(actual).toEqual(expected);
    });
});
