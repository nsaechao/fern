import { assertNever } from "@fern-api/core-utils";
import { ContainerType, Literal, MapType, NamedType, PrimitiveType, TypeReference } from "@fern-fern/ir-sdk/api";
import { csharp } from "../";
import { CodeBlock } from "../ast";
import { BaseCsharpCustomConfigSchema } from "../custom-config/BaseCsharpCustomConfigSchema";
import { AbstractCsharpGeneratorContext } from "./AbstractCsharpGeneratorContext";

export declare namespace CsharpProtobufTypeMapper {
    interface Args {
        context: AbstractCsharpGeneratorContext<BaseCsharpCustomConfigSchema>;
    }

    interface Property {
        propertyName: string;
        typeReference: TypeReference;
    }

    enum WrapperType {
        OPTIONAL,
        LIST,
        MAP
    }
}

export class CsharpProtobufTypeMapper {
    private context: AbstractCsharpGeneratorContext<BaseCsharpCustomConfigSchema>;

    constructor({ context }: CsharpProtobufTypeMapper.Args) {
        this.context = context;
    }

    public toProto({
        classReference,
        protobufType,
        properties
    }: {
        classReference: csharp.ClassReference;
        protobufType: csharp.Type;
        properties: CsharpProtobufTypeMapper.Property[];
    }): csharp.Method {
        return csharp.method({
            name: "ToProto",
            access: "internal",
            isAsync: false,
            return_: protobufType,
            parameters: [
                csharp.parameter({
                    name: "value",
                    type: csharp.Type.reference(classReference)
                })
            ],
            body: csharp.codeblock((writer) => {
                if (properties.length === 0) {
                    writer.write("return new");
                    writer.writeNode(protobufType);
                    writer.write("();");
                    return;
                }

                writer.write("var result = new");
                writer.writeNode(protobufType);
                writer.write("();");

                properties.forEach(({ propertyName, typeReference }: CsharpProtobufTypeMapper.Property) => {
                    const condition = this.toProtoCondition({ propertyName, typeReference });
                    const value = this.toProtoValueWithAssignment({ propertyName, typeReference });
                    if (condition != null) {
                        writer.controlFlow("if", condition);
                        writer.writeNodeStatement(value);
                        writer.endControlFlow();
                        return;
                    }
                    writer.write(`result.${propertyName} = `);
                    writer.writeNodeStatement(value);
                });

                writer.writeLine("return result;");
            })
        });
    }

    private toProtoCondition({
        propertyName,
        typeReference
    }: {
        propertyName: string;
        typeReference: TypeReference;
    }): CodeBlock | undefined {
        const conditions = this.getToProtoConditions({ propertyName, typeReference });
        if (conditions.length === 0) {
            return undefined;
        }
        return csharp.codeblock((writer) => {
            writer.controlFlow("if", csharp.and({ conditions }));
        });
    }

    private getToProtoConditions({
        propertyName,
        typeReference
    }: {
        propertyName: string;
        typeReference: TypeReference;
    }): CodeBlock[] {
        switch (typeReference.type) {
            case "container":
                return this.getToProtoConditionsForContainer({ propertyName, container: typeReference.container });
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

    private getToProtoConditionsForContainer({
        propertyName,
        container
    }: {
        propertyName: string;
        container: ContainerType;
    }): CodeBlock[] {
        const property = csharp.codeblock(propertyName);
        switch (container.type) {
            case "optional":
                return [
                    this.isNotNull(property),
                    ...this.getToProtoConditions({ propertyName, typeReference: container.optional })
                ];
            case "list":
            case "map":
            case "set":
                return [this.invokeAny(property)];
            case "literal":
                return [];
        }
    }

    private toProtoValueWithAssignment({
        propertyName,
        typeReference
    }: {
        propertyName: string;
        typeReference: TypeReference;
    }): CodeBlock {
        const value = this.toProtoValue({ propertyName, typeReference });
        return csharp.codeblock((writer) => {
            if (this.propertyNeedsAssignment({ typeReference })) {
                writer.write(`result.${propertyName} = `);
                writer.writeNodeStatement(value);
                return;
            }
            writer.writeNodeStatement(value);
        });
    }

    private toProtoValue({
        propertyName,
        typeReference,
        wrapperType
    }: {
        propertyName: string;
        typeReference: TypeReference;
        wrapperType?: CsharpProtobufTypeMapper.WrapperType;
    }): CodeBlock {
        switch (typeReference.type) {
            case "container":
                return this.toProtoValueForContainer({
                    propertyName,
                    container: typeReference.container
                });
            case "named":
                return this.toProtoValueForNamed({ propertyName, named: typeReference, wrapperType });
            case "primitive":
                return this.toProtoValueForPrimitive({ propertyName, primitive: typeReference.primitive, wrapperType });
            case "unknown":
                return csharp.codeblock(propertyName);
        }
    }

    private toProtoValueForNamed({
        propertyName,
        named,
        wrapperType
    }: {
        propertyName: string;
        named: NamedType;
        wrapperType?: CsharpProtobufTypeMapper.WrapperType;
    }): CodeBlock {
        if (this.context.protobufResolver.isProtobufStruct(named.typeId)) {
            return this.toProtoValueForProtobufStruct({ propertyName });
        }
        if (wrapperType == CsharpProtobufTypeMapper.WrapperType.LIST) {
            return csharp.codeblock(`${propertyName}.Select(elem => elem.ToProto())`);
        }
        return csharp.codeblock((writer) => {
            writer.writeNode(
                csharp.invokeMethod({
                    on: csharp.codeblock(propertyName),
                    method: "ToProto",
                    arguments_: []
                })
            );
        });
    }

    private toProtoValueForProtobufStruct({ propertyName }: { propertyName: string }): CodeBlock {
        return csharp.codeblock((writer) => {
            writer.writeNode(
                csharp.invokeMethod({
                    on: this.context.getProtoConverterClassReference(),
                    method: "ToProtoStruct",
                    arguments_: [csharp.codeblock(propertyName)]
                })
            );
        });
    }

    private toProtoValueForContainer({
        propertyName,
        container
    }: {
        propertyName: string;
        container: ContainerType;
    }): CodeBlock {
        switch (container.type) {
            case "optional":
                return this.toProtoValue({
                    propertyName,
                    typeReference: container.optional,
                    wrapperType: CsharpProtobufTypeMapper.WrapperType.OPTIONAL
                });
            case "list":
                return this.toProtoValueForList({ propertyName, listType: container.list });
            case "set":
                return this.toProtoValueForList({ propertyName, listType: container.set });
            case "map":
                return this.toProtoValueForMap({ propertyName, map: container });
            case "literal":
                return this.toProtoValueForLiteral({ literal: container.literal });
        }
    }

    private toProtoValueForList({
        propertyName,
        listType
    }: {
        propertyName: string;
        listType: TypeReference;
    }): CodeBlock {
        return csharp.codeblock((writer) => {
            writer.writeNode(
                csharp.invokeMethod({
                    on: csharp.codeblock(`result.${propertyName}`),
                    method: "AddRange",
                    arguments_: [
                        this.toProtoValue({
                            propertyName,
                            typeReference: listType,
                            wrapperType: CsharpProtobufTypeMapper.WrapperType.LIST
                        })
                    ]
                })
            );
        });
    }

    private toProtoValueForMap({ propertyName, map }: { propertyName: string; map: MapType }): CodeBlock {
        return csharp.codeblock((writer) => {
            writer.controlFlow("foreach", csharp.codeblock(`var kvp in ${propertyName}`));
            writer.writeNode(
                csharp.invokeMethod({
                    on: csharp.codeblock(`result.${propertyName}`),
                    method: "Add",
                    arguments_: [
                        csharp.codeblock("kvp.Key"),
                        this.toProtoValue({ propertyName, typeReference: map.valueType })
                    ]
                })
            );
        });
    }

    private toProtoValueForLiteral({ literal }: { literal: Literal }): CodeBlock {
        return csharp.codeblock((writer) => {
            switch (literal.type) {
                case "string":
                    return writer.write(`"${literal.string}"`);
                case "boolean":
                    return writer.write(literal.boolean.toString());
            }
        });
    }

    private toProtoValueForPrimitive({
        propertyName,
        primitive,
        wrapperType
    }: {
        propertyName: string;
        primitive: PrimitiveType;
        wrapperType?: CsharpProtobufTypeMapper.WrapperType;
    }): CodeBlock {
        if (wrapperType == CsharpProtobufTypeMapper.WrapperType.OPTIONAL) {
            return csharp.codeblock((writer) => {
                writer.write(propertyName);
                writer.write(" ?? ");
                writer.writeNode(this.context.getDefaultValueForPrimitive({ primitive }));
            });
        }
        return csharp.codeblock(propertyName);
    }

    private propertyNeedsAssignment({ typeReference }: { typeReference: TypeReference }): boolean {
        if (typeReference.type === "container") {
            switch (typeReference.container.type) {
                case "optional":
                    return this.propertyNeedsAssignment({ typeReference: typeReference.container.optional });
                case "list":
                case "set":
                case "map":
                    return false;
            }
        }
        return true;
    }

    private invokeAny(on: csharp.AstNode): csharp.CodeBlock {
        return csharp.codeblock((writer) => {
            writer.writeNode(
                csharp.invokeMethod({
                    on,
                    method: "Any",
                    arguments_: []
                })
            );
        });
    }

    private isNotNull(value: csharp.AstNode): csharp.CodeBlock {
        return csharp.codeblock((writer) => {
            writer.writeNode(value);
            writer.write(" != null");
        });
    }
}
