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
            const condition = this.toProtoCondition({propertyName, typeReference});
            const value = this.toProtoValue({propertyName, typeReference});
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
                return this.getToProtoConditionsForContainer({propertyName, container: typeReference.container});
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

    private getToProtoConditionsForContainer({propertyName, container}: {propertyName: string; container: ContainerType}): CodeBlock[] {
        const property = csharp.codeblock(propertyName);
        switch (container.type) {
            case "optional":
                return [
                    this.isNotNull(property),
                    ...this.getToProtoConditions({propertyName, typeReference: container.optional})
            ]
            case "list":
            case "map":
            case "set":
                return [this.invokeAny(property)]
            case "literal":
                return [];
        }
    }

    private toProtoValue({propertyName, typeReference, inList}: {propertyName: string; typeReference: TypeReference; inList?: boolean}): CodeBlock {
        switch (typeReference.type) {
            case "container":
                return this.toProtoValueForContainer({
                    propertyName,
                    container: typeReference.container,
                });
            case "named":
                return this.toProtoValueForNamed({ propertyName, named: typeReference, inList });
            case "primitive":
                return this.(reference);
            case "unknown":
                return csharp.codeblock(propertyName);
        }
    }

    private toProtoValueForNamed({propertyName, named, inList}: {propertyName: string; named: NamedType, inList?: boolean}): CodeBlock {
        if (this.context.protobufResolver.isProtobufStruct(named.typeId)) {
            return this.toProtoValueForProtobufStruct({propertyName});
        }
        if (inList) {
            return csharp.codeblock(`${propertyName}.Select(elem => elem.ToProto())`)
        }
        return csharp.codeblock((writer) => {
            writer.writeNode(
                csharp.invokeMethod({
                    on: csharp.codeblock(propertyName),
                    method: "ToProto",
                    arguments_: [],
                })
            )
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
}
