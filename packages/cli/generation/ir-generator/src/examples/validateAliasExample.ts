import { FernWorkspace } from "@fern-api/workspace-loader";
import { RawSchemas } from "@fern-api/yaml-schema";
import { FernFileContext } from "../FernFileContext";
import { ExampleResolver } from "../resolvers/ExampleResolver";
import { TypeResolver } from "../resolvers/TypeResolver";
import { ExampleViolation } from "./exampleViolation";
import { validateTypeReferenceExample } from "./validateTypeReferenceExample";

export async function validateAliasExample({
    rawAlias,
    example,
    file,
    typeResolver,
    exampleResolver,
    workspace
}: {
    rawAlias: string | RawSchemas.AliasSchema;
    example: RawSchemas.ExampleTypeValueSchema;
    file: FernFileContext;
    typeResolver: TypeResolver;
    exampleResolver: ExampleResolver;
    workspace: FernWorkspace;
}): Promise<ExampleViolation[]> {
    return await validateTypeReferenceExample({
        rawTypeReference: typeof rawAlias === "string" ? rawAlias : rawAlias.type,
        example,
        file,
        typeResolver,
        exampleResolver,
        workspace
    });
}
