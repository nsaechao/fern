import { doesPathExist, join, RelativeFilePath } from "@fern-api/fs-utils";
import { FernWorkspace } from "@fern-api/workspace-loader";
import { isRawProtobufSourceSchema, RawSchemas } from "@fern-api/yaml-schema";
import { FernFileContext } from "../FernFileContext";
import { ResolvedSource } from "./ResolvedSource";

export interface SourceResolver {
    resolveSource: (args: {
        source: RawSchemas.SourceSchema;
        file: FernFileContext;
    }) => Promise<ResolvedSource | undefined>;
    resolveSourceOrThrow: (args: { source: RawSchemas.SourceSchema; file: FernFileContext }) => Promise<ResolvedSource>;
}

export class SourceResolverImpl implements SourceResolver {
    constructor(private readonly workspace: FernWorkspace) {}

    public async resolveSourceOrThrow({
        source,
        file
    }: {
        source: RawSchemas.SourceSchema;
        file: FernFileContext;
    }): Promise<ResolvedSource> {
        const resolvedType = await this.resolveSource({ source, file });
        if (resolvedType == null) {
            const filename = isRawProtobufSourceSchema(source) ? source.proto : source.openapi;
            throw new Error(`Cannot resolve source ${filename} from file ${file.relativeFilepath}`);
        }
        return resolvedType;
    }

    public async resolveSource({
        source,
        file
    }: {
        source: RawSchemas.SourceSchema;
        file: FernFileContext;
    }): Promise<ResolvedSource | undefined> {
        if (isRawProtobufSourceSchema(source)) {
            return await this.resolveProtobufSource({ source, file });
        }
        return await this.resolveOpenAPISource({ source, file });
    }

    private async resolveProtobufSource({
        source,
        file
    }: {
        source: RawSchemas.ProtobufSourceSchema;
        file: FernFileContext;
    }): Promise<ResolvedSource | undefined> {
        const absoluteFilepath = join(this.workspace.absoluteFilepath, RelativeFilePath.of(source.proto));
        if (!(await doesPathExist(absoluteFilepath))) {
            return undefined;
        }
        return {
            type: "protobuf",
            absoluteFilePath: absoluteFilepath,
            relativeFilePath: RelativeFilePath.of(source.proto),

            // TODO: Parse the Protobuf file and include the context here.
            csharpNamespace: "",
            packageName: "",
            serviceName: ""
        };
    }

    private async resolveOpenAPISource({
        source,
        file
    }: {
        source: RawSchemas.OpenAPISourceSchema;
        file: FernFileContext;
    }): Promise<ResolvedSource | undefined> {
        const absoluteFilepath = join(this.workspace.absoluteFilepath, RelativeFilePath.of(source.openapi));
        if (!(await doesPathExist(absoluteFilepath))) {
            return undefined;
        }
        return {
            type: "openapi",
            absoluteFilePath: absoluteFilepath,
            relativeFilePath: RelativeFilePath.of(source.openapi)
        };
    }
}
