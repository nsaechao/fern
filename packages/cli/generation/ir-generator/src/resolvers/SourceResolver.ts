import { FernWorkspace } from "@fern-api/workspace-loader";
import { isRawProtobufSourceSchema, RawSchemas } from "@fern-api/yaml-schema";
import { FernFileContext } from "../FernFileContext";
import { ResolvedSource } from "./ResolvedSource";

export interface SourceResolver {
    resolveSource: (args: { source: RawSchemas.SourceSchema; file: FernFileContext }) => ResolvedSource | undefined;
    resolveSourceOrThrow: (args: { source: RawSchemas.SourceSchema; file: FernFileContext }) => ResolvedSource;
}

export class SourceResolverImpl implements SourceResolver {
    constructor(private readonly workspace: FernWorkspace) {}

    public resolveSourceOrThrow({
        source,
        file
    }: {
        source: RawSchemas.SourceSchema;
        file: FernFileContext;
    }): ResolvedSource {
        const resolvedType = this.resolveSource({ source, file });
        if (resolvedType == null) {
            const filename = isRawProtobufSourceSchema(source) ? source.proto : source.openapi;
            throw new Error(`Cannot resolve source ${filename} from file ${file.relativeFilepath}`);
        }
        return resolvedType;
    }

    public resolveSource({
        source,
        file
    }: {
        source: RawSchemas.SourceSchema;
        file: FernFileContext;
    }): ResolvedSource | undefined {
        return undefined;
    }
}
