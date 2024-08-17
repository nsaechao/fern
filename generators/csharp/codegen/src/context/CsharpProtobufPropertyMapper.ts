import { assertNever } from "@fern-api/core-utils";
import { ContainerType, Literal, MapType, NamedType, ProtobufType, TypeReference } from "@fern-fern/ir-sdk/api";
import { csharp } from "../";
import { CodeBlock } from "../ast";
import { BaseCsharpCustomConfigSchema } from "../custom-config/BaseCsharpCustomConfigSchema";
import { AbstractCsharpGeneratorContext } from "./AbstractCsharpGeneratorContext";

export declare namespace CsharpProtobufTypeMapper {
    interface Args {
        context: AbstractCsharpGeneratorContext<BaseCsharpCustomConfigSchema>;
        protobufType: ProtobufType;
    }
}

export class CsharpProtobufTypeMapper {
    private context: AbstractCsharpGeneratorContext<BaseCsharpCustomConfigSchema>;
    private protobufType: ProtobufType;

    constructor({ context, protobufType }: CsharpProtobufTypeMapper.Args) {
        this.context = context;
        this.protobufType = protobufType;
    }

    public toProto({propertyName, typeReference}: {propertyName: string; typeReference: TypeReference}): CodeBlock {
        return csharp.codeblock((writer) => {
            const value = this.toProtoValue({propertyName, typeReference});
            const condition = this.toProtoCondition({propertyName, typeReference});
            if (condition != null) {
                writer.controlFlow("if", condition)
                writer.writeNode(value);
                writer.endControlFlow();
                return;
            }
            writer.writeNode(value);
        })

    }

    private toProtoCondition({propertyName, typeReference}: {propertyName: string; typeReference: TypeReference}): CodeBlock | undefined {
        const conditions = this.getToProtoConditions({propertyName, typeReference});
        if (conditions.length === 0) {
            return undefined;
        }
        return csharp.codeblock((writer) => {
            writer.controlFlow("if", csharp.and({ conditions }))
        })
    }

    private getToProtoConditions({propertyName, typeReference}: {propertyName: string; typeReference: TypeReference}): CodeBlock[] {
        switch (typeReference.type) {
            case "container":
                const property = csharp.codeblock(propertyName);
                switch (typeReference.container.type) {
                    case "optional":
                        return [
                            this.isNotNull(property),
                            ...this.getToProtoConditions({propertyName, typeReference: typeReference.container.optional})
                    ]
                    case "list":
                    case "map":
                    case "set":
                        return [this.invokeAny(property)]
                    case "literal":
                        return [];
                }
            case "named":
                return [];
            case "primitive":
                return [];
            case "unknown":
                return [];
            default:
                assertNever(typeReference);
        }
    }

    private toProtoValue({propertyName, typeReference}: {propertyName: string; typeReference: TypeReference}): CodeBlock {
        switch (typeReference.type) {
            case "container":
                return this.toProtoValueForContainer({
                    propertyName,
                    container: typeReference.container,
                });
            case "named":
                return this.toProtoValueForNamed({ named: reference });
            case "primitive":
                return this.(reference);
            case "unknown":
                return csharp.Type.object();
            default:
                assertNever(reference);
        }
    }

    private toProtoValueForNamed({propertyName, named}: {propertyName: string; named: NamedType}): CodeBlock {
        if (this.context.protobufResolver.isProtobufStruct(named.typeId)) {
            return this.toProtoValueForProtobufStruct({propertyName});
        }
        return csharp.codeblock((writer) => {

        })
    }
    
    private toProtoValueForProtobufStruct({propertyName}: {propertyName: string}): CodeBlock {
        return csharp.codeblock((writer) => {
            writer.writeNode(
                csharp.invokeMethod({
                    on: this.context.getProtoConverterClassReference(),
                    method: "ToProtoStruct",
                    arguments_: [
                        csharp.codeblock(propertyName),
                    ]
                })
            )
        })
    }

    private toProtoValueForContainer({propertyName, container}: {propertyName: string; container: ContainerType}): CodeBlock {
        switch (container.type) {
            case "optional":
                return this.toProtoValue({propertyName, typeReference: container.optional});
            case "list":
                return this.toProtoValueForList({propertyName, listType: container.list});
            case "set":
                return this.toProtoValueForList({propertyName, listType: container.set});
            case "map":
                return this.toProtoValueForMap({propertyName, map: container});
            case "literal":
                return this.toProtoValueForLiteral({literal: container.literal});
        }
    }

    private toProtoValueForList({propertyName, listType}: {propertyName: string; listType: TypeReference}): CodeBlock {
        return csharp.codeblock((writer) => {
            writer.writeNode(
                csharp.invokeMethod({
                    on: csharp.codeblock(`result.${propertyName}`),
                    method: "AddRange",
                    arguments_: [
                        // TODO: We might need to propagate details that this is within an AddRange statement.
                        // This affects how named types are mapped, and even whether or not we need a default
                        // value for primitives.
                        this.toProtoValue({propertyName, typeReference: listType}),
                    ],
                })
            )
        });
    }

    private toProtoValueForMap({propertyName, map}: {propertyName: string; map: MapType}): CodeBlock {
        return csharp.codeblock((writer) => {
            writer.controlFlow("foreach", csharp.codeblock(`var kvp in ${propertyName}`));
            writer.writeNode(
                csharp.invokeMethod({
                    on: csharp.codeblock(`result.${propertyName}`),
                    method: "Add",
                    arguments_: [
                        csharp.codeblock("kvp.Key"),
                        this.toProtoValue({propertyName, typeReference: map.valueType}),
                    ],
                })
            )
        })
    }

    private toProtoValueForLiteral({literal}: {literal: Literal}): CodeBlock {
        return csharp.codeblock((writer) => {
            switch (literal.type) {
                case "string":
                    return writer.write(`"${literal.string}"`);
                case "boolean":
                    return writer.write(literal.boolean.toString());
            }
        });
    }


    // private toProtoPropertyMapperForRequired({
    //     propertyName,
    //     mapperType
    // }: {
    //     propertyName: string;
    //     mapperType: MapperType;
    // }): csharp.CodeBlock {
    //     switch (mapperType) {
    //         case "primitive":
    //             return csharp.codeblock((writer) => writer.writeLine(`${propertyName} = ${propertyName};`));
    //         case "named":
    //             return csharp.codeblock("TODO");
    //         case "list":
    //             return csharp.codeblock((writer) => {
    //                 writer.write("if (");
    //                 writer.writeNode(this.invokeAny(csharp.codeblock(propertyName)));
    //                 writer.write(") {");
    //                 writer.indent();
    //                 writer.writeLine(`result.${propertyName}.AddRange(${propertyName})`);
    //                 writer.dedent();
    //             });
    //         case "map":
    //             return csharp.codeblock("TODO");
    //         case "unknown":
    //             return csharp.codeblock("TODO");
    //     }
    // }

    // private toProtoPropertyMapperForOptional({
    //     propertyName,
    //     mapperType
    // }: {
    //     propertyName: string;
    //     mapperType: MapperType;
    // }): csharp.CodeBlock {
    //     switch (mapperType) {
    //         case "primitive":
    //             return csharp.codeblock("TODO");
    //         case "named":
    //             return csharp.codeblock((writer) =>
    //                 writer.writeLine(`result.${propertyName} = ${propertyName}.ToProto()`)
    //             );
    //         case "list":
    //             return csharp.codeblock("TODO");
    //         case "map":
    //             return csharp.codeblock("TODO");
    //         case "unknown":
    //             return csharp.codeblock("TODO");
    //     }
    // }

    private invokeAny(on: csharp.AstNode): csharp.CodeBlock {
        return csharp.codeblock((writer) => {
            writer.writeNode(
                csharp.invokeMethod({
                    on,
                    method: "Any",
                    arguments_: []
                }),
            );
        });
    }
    
    private isNotNull(value: csharp.AstNode): csharp.CodeBlock {
        return csharp.codeblock((writer) => {
            writer.writeNode(value);
            writer.write(" != null");
        })
    }

    // private convertContainer({
    //     container,
    //     unboxOptionals
    // }: {
    //     container: ContainerType;
    //     unboxOptionals: boolean;
    // }): Type {
    //     switch (container.type) {
    //         case "list":
    //             return Type.list(this.convert({ reference: container.list, unboxOptionals: true }));
    //         case "map": {
    //             const key = this.convert({ reference: container.keyType });
    //             const value = this.convert({ reference: container.valueType });
    //             if (value.internalType.type === "object") {
    //                 // object map values should be nullable.
    //                 return Type.map(key, csharp.Type.optional(value));
    //             }
    //             return Type.map(key, value);
    //         }
    //         case "set":
    //             return Type.set(this.convert({ reference: container.set, unboxOptionals: true }));
    //         case "optional":
    //             return unboxOptionals
    //                 ? this.convert({ reference: container.optional, unboxOptionals })
    //                 : Type.optional(this.convert({ reference: container.optional }));
    //         case "literal":
    //             return this.convertLiteral({ literal: container.literal });
    //         default:
    //             assertNever(container);
    //     }
    // }

    // private convertPrimitive({ primitive }: { primitive: PrimitiveType }): Type {
    //     return PrimitiveTypeV1._visit<csharp.Type>(primitive.v1, {
    //         integer: () => csharp.Type.integer(),
    //         long: () => csharp.Type.long(),
    //         uint: () => csharp.Type.uint(),
    //         uint64: () => csharp.Type.ulong(),
    //         float: () => csharp.Type.float(),
    //         double: () => csharp.Type.double(),
    //         boolean: () => csharp.Type.boolean(),
    //         string: () => csharp.Type.string(),
    //         date: () => csharp.Type.date(),
    //         dateTime: () => csharp.Type.dateTime(),
    //         uuid: () => csharp.Type.string(),
    //         // https://learn.microsoft.com/en-us/dotnet/api/system.convert.tobase64string?view=net-8.0
    //         base64: () => csharp.Type.string(),
    //         bigInteger: () => csharp.Type.string(),
    //         _other: () => csharp.Type.object()
    //     });
    // }

    // private convertLiteral({ literal }: { literal: Literal }): Type {
    //     switch (literal.type) {
    //         case "boolean":
    //             return csharp.Type.boolean();
    //         case "string":
    //             return csharp.Type.string();
    //     }
    // }

    // private convertNamed({ named }: { named: DeclaredTypeName }): Type {
    //     const objectClassReference = this.convertToClassReference(named);
    //     const typeDeclaration = this.context.getTypeDeclarationOrThrow(named.typeId);

    //     if (this.context.protobufResolver.isProtobufStruct(typeDeclaration.name.typeId)) {
    //         return this.context.protobufResolver.getProtobufStructTypeOrThrow();
    //     }

    //     if (this.context.protobufResolver.isProtobufValue(typeDeclaration.name.typeId)) {
    //         return this.context.protobufResolver.getProtobufValueTypeOrThrow();
    //     }

    //     switch (typeDeclaration.shape.type) {
    //         case "alias":
    //             return this.convert({ reference: typeDeclaration.shape.aliasOf });
    //         case "enum":
    //             return csharp.Type.reference(objectClassReference);
    //         case "object":
    //             return csharp.Type.reference(objectClassReference);
    //         case "union":
    //             return csharp.Type.object();
    //         case "undiscriminatedUnion": {
    //             return csharp.Type.oneOf(
    //                 typeDeclaration.shape.members.map((member) => {
    //                     return this.convert({ reference: member.type });
    //                 })
    //             );
    //         }
    //         default:
    //             assertNever(typeDeclaration.shape);
    //     }
    // }
}
