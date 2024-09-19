import { TypeReference } from "@fern-fern/ir-sdk/api";
import { PayloadLocation, Template, TemplateInput } from "@fern-fern/snippet-sdk/api";

export declare namespace AbstractTemplateGenerator {
    interface Args {
        /* Where the data for this template lives */
        location: PayloadLocation;
        /* The path up till this template (e.g. data.person.id */
        path: string[];
        /* The key that this template is under */
        propertyKey?: string;
    }
}

export const TEMPLATE_SENTINEL = "$FERN_INPUT";

export abstract class AbstractTemplateGenerator {
    protected location: PayloadLocation;
    protected path: string[];
    protected propertyKey: string | undefined;

    public constructor({ location, path, propertyKey }: AbstractTemplateGenerator.Args) {
        this.location = location;
        this.path = path;
        this.propertyKey = propertyKey;
    }

    public abstract generate(): Template;

    protected getPath(): string[] {
        if (this.propertyKey == null) {
            return this.path;
        } else {
            return [...this.path, this.propertyKey];
        }
    }

    protected getTemplateInputFromTypeReference({ typeReference }: { typeReference: TypeReference }): TemplateInput {
        return typeReference._visit({
            primitive: () =>
                Template.generic({
                    imports: [],
                    templateString: `${TEMPLATE_SENTINEL}`,
                    isOptional: true,
                    templateInputs: [
                        TemplateInput.payload({
                            location: this.location,
                            path: this.getPath().join(".")
                        })
                    ]
                }),
            unknown: () =>
                Template.generic({
                    imports: [],
                    templateString: `${TEMPLATE_SENTINEL}`,
                    isOptional: true,
                    templateInputs: [
                        TemplateInput.payload({
                            location: this.location,
                            path: this.getPath().join(".")
                        })
                    ]
                }),
            container: (containerType) =>
                this.getContainerTemplate({
                    containerType,
                    name,
                    location,
                    wireOrOriginalName,
                    nameBreadcrumbs,
                    indentationLevel,
                    isObjectInlined,
                    includeLiteralTemplates
                }),
            named: (typeName) =>
                this.getNamedTypeTemplate({
                    typeName,
                    name,
                    location,
                    wireOrOriginalName,
                    nameBreadcrumbs,
                    indentationLevel,
                    isObjectInlined,
                    includeLiteralTemplates
                }),
            _other: () => undefined
        });
    }
}
