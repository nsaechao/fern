import { ObjectTypeDeclaration } from "@fern-fern/ir-sdk/api";
import { Template, TemplateInput } from "@fern-fern/snippet-sdk/api";
import { AbstractTemplateGenerator, TEMPLATE_SENTINEL } from "./AbstractTemplateGenerator";

export declare namespace ObjectTemplateGenerator {
    interface Args extends AbstractTemplateGenerator.Args {
        typeDeclaration: ObjectTypeDeclaration;
    }
}

export class EnumTemplateGenerator extends AbstractTemplateGenerator {
    private typeDeclaration: ObjectTypeDeclaration;

    public constructor({ typeDeclaration, ...superArgs }: ObjectTemplateGenerator.Args) {
        super(superArgs);
        this.typeDeclaration = typeDeclaration;
    }

    public generate(): Template {
        const properties: TemplateInput[] = [];
        for (const property of this.typeDeclaration.properties) {
            const propInput = this.getTemplateInputFromTypeReference({
                typeReference: prop.valueType,
                name: this.getPropertyKey(prop.name.name),
                location,
                wireOrOriginalName: prop.name.wireValue,
                nameBreadcrumbs: childBreadcrumbs,
                indentationLevel: childIndentationLevel,
                isObjectInlined: false
            });
        }
        return FdrSnippetTemplate.Template.generic({
            imports: [],
            // If the object is inlined, we don't need to wrap it in JSON object notation.
            // Mostly useful for discriminated union types which otherwise would be wrapped in an object [FER-1986]
            templateString: isObjectInlined
                ? this.getAsNamedParameterTemplate(name, `${TEMPLATE_SENTINEL}`)
                : this.getAsNamedParameterTemplate(name, `{\n${childTabs}${TEMPLATE_SENTINEL}\n${selfTabs}}`),
            isOptional: true,
            inputDelimiter: `,\n${childTabs}`,
            templateInputs
        });
    }
}
