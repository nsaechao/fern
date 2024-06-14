import { FernFilepath } from "@fern-api/ir-sdk";

export type AudienceId = string;
export type TypeId = string;
export type ErrorId = string;
export type ServiceId = string;
export type EndpointId = string;
export type SubpackageId = string;
export type WebhookId = string;

export interface TypeNode {
    typeId: TypeId;
    allDescendants: Set<TypeId>;
    /* Only populated if the type has properties with audiences */
    descendantsByAudience: Record<AudienceId, Set<TypeId>>;
    referencedSubpackages: Set<FernFilepath>;
}

export interface TypePropertiesNode {
    typeId: TypeId;
    /* If audience not present, keep all properties */
    propertiesByAudience: Record<AudienceId, Set<string>>;
}

export interface InlinedRequestPropertiesNode {
    endpointId: EndpointId;
    /* If audience not present, keep all properties */
    propertiesByAudience: Record<AudienceId, Set<string>>;
}

export interface InlinedWebhookPayloadProperiesNode {
    webhookId: WebhookId;
    /* If audience not present, keep all properties */
    propertiesByAudience: Record<AudienceId, Set<string>>;
}

export interface ErrorNode {
    errorId: ErrorId;
    referencedTypes: Set<TypeId>;
    referencedSubpackages: Set<FernFilepath>;
}

export interface EndpointNode {
    endpointId: EndpointId;
    referencedErrors: Set<ErrorId>;
    referencedTypes: Set<TypeId>;
    referencedSubpackages: Set<FernFilepath>;
}
export interface WebhookNode {
    webhookId: WebhookId;
    referencedTypes: Set<TypeId>;
    referencedSubpackages: Set<FernFilepath>;
}
