/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as FernOpenapiIr from "../../../../api";
import * as core from "../../../../core";

export const UnDiscriminatedOneOfSchema: core.serialization.ObjectSchema<
    serializers.UnDiscriminatedOneOfSchema.Raw,
    FernOpenapiIr.UnDiscriminatedOneOfSchema
> = core.serialization
    .objectWithoutOptionalProperties({
        schemas: core.serialization.list(core.serialization.lazy(async () => (await import("../../..")).Schema)),
        examples: core.serialization
            .list(core.serialization.lazy(async () => (await import("../../..")).FullExample))
            .optional(),
    })
    .extend(core.serialization.lazyObject(async () => (await import("../../..")).WithDescription))
    .extend(core.serialization.lazyObject(async () => (await import("../../..")).WithName))
    .extend(core.serialization.lazyObject(async () => (await import("../../..")).WithSdkGroupName))
    .extend(core.serialization.lazyObject(async () => (await import("../../..")).WithAvailability));

export declare namespace UnDiscriminatedOneOfSchema {
    interface Raw
        extends serializers.WithDescription.Raw,
            serializers.WithName.Raw,
            serializers.WithSdkGroupName.Raw,
            serializers.WithAvailability.Raw {
        schemas: serializers.Schema.Raw[];
        examples?: serializers.FullExample.Raw[] | null;
    }
}
