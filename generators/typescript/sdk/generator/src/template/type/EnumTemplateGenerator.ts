import { EnumTypeDeclaration } from "@fern-fern/ir-sdk/api";
import { Template, TemplateInput } from "@fern-fern/snippet-sdk/api";
import { AbstractTemplateGenerator, TEMPLATE_SENTINEL } from "./AbstractTemplateGenerator";

export declare namespace EnumTemplateGenerator {
    interface Args extends AbstractTemplateGenerator.Args {
        typeDeclaration: EnumTypeDeclaration;
    }
}

export class EnumTemplateGenerator extends AbstractTemplateGenerator {
    private typeDeclaration: EnumTypeDeclaration;

    public constructor({ typeDeclaration, ...superArgs }: EnumTemplateGenerator.Args) {
        super(superArgs);
        this.typeDeclaration = typeDeclaration;
    }

    public generate(): Template {
        return Template.enum({
            imports: [],
            isOptional: true,
            values: Object.fromEntries(
                this.typeDeclaration.values.map((enumValue) => [enumValue.name.wireValue, enumValue.name.wireValue])
            ),
            templateString: `${TEMPLATE_SENTINEL}`,
            templateInput: TemplateInput.payload({
                location: this.location,
                path: this.getPath().join(".")
            })
        });
    }
}
