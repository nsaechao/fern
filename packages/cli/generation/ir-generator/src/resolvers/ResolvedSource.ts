import { AbsoluteFilePath, RelativeFilePath } from "@fern-api/fs-utils";
import { Source } from "@fern-api/ir-sdk";

export declare type ResolvedSource = ResolvedSource.OpenAPI | ResolvedSource.Protobuf;

export declare namespace ResolvedSource {
    interface OpenAPI {
        type: "openapi";
        absoluteFilePath: AbsoluteFilePath;
        relativeFilePath: RelativeFilePath;
    }

    interface Protobuf {
        type: "protobuf";
        absoluteFilePath: AbsoluteFilePath;
        relativeFilePath: RelativeFilePath;
        csharpNamespace: string | undefined;
        packageName: string | undefined;
        serviceName: string | undefined;
    }
}

export function convertResolvedSourceToSource(resolvedSource: ResolvedSource): Source | undefined {
    if (resolvedSource.type === "openapi") {
        return undefined;
    }

    // TODO: Map to a user-defined Protobuf type.
    //
    // TODO: How should we model this with services?
    return Source.proto({});
}
