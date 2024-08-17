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
            // const protobufMapper = new CsharpProtobufTypeMapper();
            class_.addMethod(
                this.getToProtoMethod({
                    protobufType,
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

    private getToProtoMethod({
        protobufType,
        properties
    }: {
        protobufType: csharp.Type;
        properties: ObjectProperty[];
    }): csharp.Method {
        return csharp.method({
            name: "ToProto",
            access: "internal",
            isAsync: false,
            return_: protobufType,
            parameters: [
                csharp.parameter({
                    name: "value",
                    type: csharp.Type.reference(this.classReference)
                })
            ],
            body: 
        });
    }

    private getFromProtoMethod({
        protobufType,
        properties
    }: {
        protobufType: ProtobufType;
        properties: ObjectProperty[];
    }): csharp.Method {
        return csharp.method({
            name: "FromProto",
            access: "internal",
            type: MethodType.STATIC,
            return_: csharp.Type.reference(this.classReference),
            isAsync: false,
            parameters: [],
            body: csharp.codeblock((writer) => {
                /* TODO */
            })
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
