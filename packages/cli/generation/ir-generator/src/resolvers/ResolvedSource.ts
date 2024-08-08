import { AbsoluteFilePath, RelativeFilePath } from "@fern-api/fs-utils";

export declare type ResolvedSource = ResolvedSource.OpenAPI | ResolvedSource.Protobuf;

export declare namespace ResolvedSource {
    interface OpenAPI {
        _type: "openapi";
        absoluteFilePath: AbsoluteFilePath;
        relativeFilePath: RelativeFilePath;
    }

    interface Protobuf {
        _type: "protobuf";
        absoluteFielPath: AbsoluteFilePath;
        relativeFilePath: RelativeFilePath;

        // TODO: Should these use the IR name representation?
        csharpNamespace: string | undefined;
        packageName: string | undefined;
        serviceName: string | undefined;
    }
}
