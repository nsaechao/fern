import { isPlainObject } from "@fern-api/core-utils";
import { FernWorkspace } from "@fern-api/workspace-loader";
import { isRawObjectDefinition, RawSchemas } from "@fern-api/yaml-schema";
import { getUnionDiscriminant } from "../converters/type-declarations/convertDiscriminatedUnionTypeDeclaration";
import { FernFileContext } from "../FernFileContext";
import { ExampleResolver } from "../resolvers/ExampleResolver";
import { TypeResolver } from "../resolvers/TypeResolver";
import { ExampleViolation } from "./exampleViolation";
import { getViolationsForMisshapenExample } from "./getViolationsForMisshapenExample";
import { validateObjectExample } from "./validateObjectExample";
import { validateTypeReferenceExample } from "./validateTypeReferenceExample";

export async function validateUnionExample({
    typeName,
    rawUnion,
    example,
    typeResolver,
    exampleResolver,
    file,
    workspace
}: {
    typeName: string;
    rawUnion: RawSchemas.DiscriminatedUnionSchema;
    example: RawSchemas.ExampleTypeValueSchema;
    typeResolver: TypeResolver;
    exampleResolver: ExampleResolver;
    file: FernFileContext;
    workspace: FernWorkspace;
}): Promise<ExampleViolation[]> {
    if (!isPlainObject(example)) {
        return getViolationsForMisshapenExample(example, "an object");
    }

    const discriminant = getUnionDiscriminant(rawUnion);
    const { [discriminant]: discriminantValue, ...nonDiscriminantPropertyExamples } = example;

    if (discriminantValue == null) {
        return [
            {
                message: `Missing discriminant property ("${discriminant}")`
            }
        ];
    }

    if (typeof discriminantValue !== "string") {
        return getViolationsForMisshapenExample(discriminantValue, "a string");
    }

    const singleUnionTypeDefinition = rawUnion.union[discriminantValue];
    if (singleUnionTypeDefinition == null) {
        return [
            {
                message:
                    `Invalid discriminant property: "${discriminantValue}". Allowed discriminant values:\n` +
                    Object.keys(rawUnion.union)
                        .map((otherDiscriminantValue) => `  - ${otherDiscriminantValue}`)
                        .join("\n")
            }
        ];
    }

    const type =
        typeof singleUnionTypeDefinition === "string" ? singleUnionTypeDefinition : singleUnionTypeDefinition.type;

    if (typeof type !== "string") {
        return getRuleViolationForExtraProperties(nonDiscriminantPropertyExamples);
    }

    const resolvedType = await typeResolver.resolveType({
        type,
        file
    });

    // type doesn't exist. this is handled by other rules
    if (resolvedType == null) {
        return [];
    }

    if (resolvedType._type === "named" && isRawObjectDefinition(resolvedType.declaration)) {
        return await validateObjectExample({
            typeName,
            typeNameForBreadcrumb: typeName,
            rawObject: resolvedType.declaration,
            file: resolvedType.file,
            example: nonDiscriminantPropertyExamples,
            typeResolver,
            exampleResolver,
            workspace
        });
    }

    const singlePropertyKey =
        typeof singleUnionTypeDefinition !== "string" && typeof singleUnionTypeDefinition.key === "string"
            ? singleUnionTypeDefinition.key
            : undefined;

    // "key" is not defined, but this will be caught by other rules
    if (singlePropertyKey == null) {
        return [];
    }

    const { [singlePropertyKey]: singlePropertyExample, ...extraProperties } = nonDiscriminantPropertyExamples;

    const violations: ExampleViolation[] = [];
    if (singlePropertyExample == null) {
        violations.push({
            message: `Missing property "${singlePropertyKey}"`
        });
    } else {
        violations.push(
            ...validateTypeReferenceExample({
                rawTypeReference: type,
                example: singlePropertyExample,
                typeResolver,
                exampleResolver,
                file,
                workspace
            })
        );
    }

    violations.push(...getRuleViolationForExtraProperties(extraProperties));

    return violations;
}

function getRuleViolationForExtraProperties(extraProperties: Record<string, unknown>): ExampleViolation[] {
    return Object.keys(extraProperties).map((key) => ({
        severity: "error",
        message: `Unexpected property "${key}"`
    }));
}
