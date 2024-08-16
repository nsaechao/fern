import { csharp, CSharpFile, FileGenerator } from "@fern-api/csharp-codegen";
import { MethodType } from "@fern-api/csharp-codegen/src/ast";
import { join, RelativeFilePath } from "@fern-api/fs-utils";
import {
    ExampleObjectType,
    NameAndWireValue,
    ObjectProperty,
    ObjectTypeDeclaration,
    TypeDeclaration
} from "@fern-fern/ir-sdk/api";
import { ModelCustomConfigSchema } from "../ModelCustomConfig";
import { ModelGeneratorContext } from "../ModelGeneratorContext";
import { ExampleGenerator } from "../snippets/ExampleGenerator";
import { getUndiscriminatedUnionSerializerAnnotation } from "../undiscriminated-union/getUndiscriminatedUnionSerializerAnnotation";

// TODO: Add support for protobufStruct.
type MapperType = "primitive" | "named" | "list" | "map" | "unknown";

export class ObjectGenerator extends FileGenerator<CSharpFile, ModelCustomConfigSchema, ModelGeneratorContext> {
    private readonly typeDeclaration: TypeDeclaration;
    private readonly classReference: csharp.ClassReference;
    private readonly exampleGenerator: ExampleGenerator;
    constructor(
        context: ModelGeneratorContext,
        typeDeclaration: TypeDeclaration,
        private readonly objectDeclaration: ObjectTypeDeclaration
    ) {
        super(context);
        this.typeDeclaration = typeDeclaration;
        this.classReference = this.context.csharpTypeMapper.convertToClassReference(this.typeDeclaration.name);
        this.exampleGenerator = new ExampleGenerator(context);
    }

    public doGenerate(): CSharpFile {
        const class_ = csharp.class_({
            ...this.classReference,
            partial: false,
            access: "public",
            record: true
        });
        const flattenedProperties = [
            ...this.objectDeclaration.properties,
            ...(this.objectDeclaration.extendedProperties ?? [])
        ];
        flattenedProperties.forEach((property) => {
            const annotations: csharp.Annotation[] = [];
            const maybeUndiscriminatedUnion = this.context.getAsUndiscriminatedUnionTypeDeclaration(property.valueType);
            if (maybeUndiscriminatedUnion != null) {
                annotations.push(
                    getUndiscriminatedUnionSerializerAnnotation({
                        context: this.context,
                        undiscriminatedUnionDeclaration: maybeUndiscriminatedUnion.declaration,
                        isList: maybeUndiscriminatedUnion.isList
                    })
                );
            }

            class_.addField(
                csharp.field({
                    name: this.getPropertyName({ className: this.classReference.name, objectProperty: property.name }),
                    type: this.context.csharpTypeMapper.convert({ reference: property.valueType }),
                    access: "public",
                    get: true,
                    set: true,
                    summary: property.docs,
                    jsonPropertyName: property.name.wireValue,
                    annotations,
                    useRequired: true
                })
            );
        });

        if (this.shouldGenerateProtobufMappers(this.typeDeclaration)) {
            const protobufType = this.context.protobufResolver.getProtobufTypeOrThrow(this.typeDeclaration.name.typeId);
            class_.addMethod(
                this.getToProtoMethod({
                    properties: flattenedProperties
                })
            );
            class_.addMethod(
                this.getFromProtoMethod({
                    properties: flattenedProperties
                })
            );
        }

        return new CSharpFile({
            clazz: class_,
            directory: this.context.getDirectoryForTypeId(this.typeDeclaration.name.typeId),
            allNamespaceSegments: this.context.getAllNamespaceSegments(),
            allTypeClassReferences: this.context.getAllTypeClassReferences(),
            namespace: this.context.getNamespace(),
            customConfig: this.context.customConfig
        });
    }

    public doGenerateSnippet(exampleObject: ExampleObjectType): csharp.CodeBlock {
        const args = exampleObject.properties.map((exampleProperty) => {
            const propertyName = this.getPropertyName({
                className: this.classReference.name,
                objectProperty: exampleProperty.name
            });
            const assignment = this.exampleGenerator.getSnippetForTypeReference(exampleProperty.value);
            // todo: considering filtering out "assignments" are are actually just null so that null properties
            // are completely excluded from object initializers
            return { name: propertyName, assignment };
        });
        const instantiateClass = csharp.instantiateClass({
            classReference: this.classReference,
            arguments_: args
        });
        return csharp.codeblock((writer) => writer.writeNode(instantiateClass));
    }

    private getToProtoMethod({ properties }: { properties: ObjectProperty[] }): csharp.Method {
        return csharp.method({
            name: "ToProto",
            access: "internal",
            isAsync: false,
            return_: this.context.protobufResolver.getProtobufTypeOrThrow(this.typeDeclaration.name.typeId),
            parameters: [
                csharp.parameter({
                    name: "value",
                    type: csharp.Type.reference(this.classReference)
                })
            ]
        });
    }

    // TODO: Handle required -> optional case.
    // TODO: Handle optional -> optional case.
    // TODO: Handle required list -> optional list case.
    // TODO: Handle optional list -> optional list case.
    // TODO: Handle struct -> optional struct case.
    // TODO: Handle optional struct -> optional struct case.
    private toProtoPropertyMapper({ property }: { property: ObjectProperty }): csharp.CodeBlock {
        const propertyName = this.getPropertyName({
            className: this.classReference.name,
            objectProperty: property.name
        });
        const mapperType = this.getMapperType(property);
        const isOptional = this.context.isOptional(property.valueType);
        if (isOptional) {
            return this.toProtoPropertyMapperForOptional({
                propertyName,
                mapperType
            });
        }
        return this.toProtoPropertyMapperForRequired({
            propertyName,
            mapperType
        });
    }

    private toProtoPropertyMapperForRequired({
        propertyName,
        mapperType
    }: {
        propertyName: string;
        mapperType: MapperType;
    }): csharp.CodeBlock {
        switch (mapperType) {
            case "primitive":
                return csharp.codeblock((writer) => writer.writeLine(`${propertyName} = ${propertyName};`));
            case "named":
                return csharp.codeblock("TODO");
            case "list":
                return csharp.codeblock((writer) => {
                    writer.write("if (");
                    writer.writeNode(this.invokeAny(csharp.codeblock(propertyName)));
                    writer.write(") {");
                    writer.indent();
                    writer.writeLine(`result.${propertyName}.AddRange(${propertyName})`);
                    writer.dedent();
                });
            case "map":
                return csharp.codeblock("TODO");
            case "unknown":
                return csharp.codeblock("TODO");
        }
    }

    private toProtoPropertyMapperForOptional({
        propertyName,
        mapperType
    }: {
        propertyName: string;
        mapperType: MapperType;
    }): csharp.CodeBlock {
        switch (mapperType) {
            case "primitive":
                return csharp.codeblock("TODO");
            case "named":
                return csharp.codeblock((writer) =>
                    writer.writeLine(`result.${propertyName} = ${propertyName}.ToProto()`)
                );
            case "list":
                return csharp.codeblock("TODO");
            case "map":
                return csharp.codeblock("TODO");
            case "unknown":
                return csharp.codeblock("TODO");
        }
    }

    private getFromProtoMethod({ properties }: { properties: ObjectProperty[] }): csharp.Method {
        return csharp.method({
            name: "FromProto",
            access: "internal",
            type: MethodType.STATIC,
            return_: csharp.Type.reference(this.classReference),
            isAsync: false,
            parameters: []
        });
    }

    private invokeAny(on: csharp.AstNode): csharp.MethodInvocation {
        return csharp.invokeMethod({
            on,
            method: "Any",
            arguments_: []
        });
    }

    /**
     * Class Names and Property Names cannot overlap in C# otherwise there are compilation errors.
     */
    private getPropertyName({
        className,
        objectProperty
    }: {
        className: string;
        objectProperty: NameAndWireValue;
    }): string {
        const propertyName = this.context.getPascalCaseSafeName(objectProperty.name);
        if (propertyName === className) {
            return `${propertyName}_`;
        }
        return propertyName;
    }

    private getMapperType(property: ObjectProperty): MapperType {
        if (this.context.isPrimitive(property.valueType)) {
            return "primitive";
        }
        if (this.context.isNamed(property.valueType)) {
            return "named";
        }
        if (this.context.isList(property.valueType)) {
            return "list";
        }
        if (this.context.isMap(property.valueType)) {
            return "map";
        }
        return "unknown";
    }

    private shouldGenerateProtobufMappers(typeDeclaration: TypeDeclaration): boolean {
        return typeDeclaration.encoding?.proto != null;
    }

    protected getFilepath(): RelativeFilePath {
        return join(
            this.context.project.filepaths.getSourceFileDirectory(),
            RelativeFilePath.of(this.classReference.name + ".cs")
        );
    }
}
