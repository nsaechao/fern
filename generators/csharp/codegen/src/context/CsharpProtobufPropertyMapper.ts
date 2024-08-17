import { assertNever } from "@fern-api/core-utils";
import {
    ContainerType,
    Literal,
    MapType,
    NamedType,
    PrimitiveType,
    ProtobufType,
    TypeReference
} from "@fern-fern/ir-sdk/api";
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

enum WrapperType {
    OPTIONAL,
    LIST,
    MAP
}

export class CsharpProtobufTypeMapper {
    private context: AbstractCsharpGeneratorContext<BaseCsharpCustomConfigSchema>;
    private protobufType: ProtobufType;

    constructor({ context, protobufType }: CsharpProtobufTypeMapper.Args) {
        this.context = context;
        this.protobufType = protobufType;
    }

    // TODO: Should this method handle the whole body, or just each property individually?
    public toProto({ propertyName, typeReference }: { propertyName: string; typeReference: TypeReference }): CodeBlock {
        return csharp.codeblock((writer) => {
            const condition = this.toProtoCondition({ propertyName, typeReference });
            const value = this.toProtoValue({ propertyName, typeReference });
            if (condition != null) {
                writer.controlFlow("if", condition);
                writer.writeNode(value);
                writer.endControlFlow();
                return;
            }
            writer.writeNode(value);
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

    private toProtoValue({
        propertyName,
        typeReference,
        wrapperType
    }: {
        propertyName: string;
        typeReference: TypeReference;
        wrapperType?: WrapperType;
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
        wrapperType?: WrapperType;
    }): CodeBlock {
        if (this.context.protobufResolver.isProtobufStruct(named.typeId)) {
            return this.toProtoValueForProtobufStruct({ propertyName });
        }
        if (wrapperType == WrapperType.LIST) {
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
                    wrapperType: WrapperType.OPTIONAL
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
                        this.toProtoValue({ propertyName, typeReference: listType, wrapperType: WrapperType.LIST })
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
        wrapperType?: WrapperType;
    }): CodeBlock {
        if (wrapperType == WrapperType.OPTIONAL) {
            return csharp.codeblock((writer) => {
                writer.write(propertyName);
                writer.write(" ?? ");
                writer.writeNode(this.context.getDefaultValueForPrimitive({ primitive }));
            });
        }
        return csharp.codeblock(propertyName);
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
