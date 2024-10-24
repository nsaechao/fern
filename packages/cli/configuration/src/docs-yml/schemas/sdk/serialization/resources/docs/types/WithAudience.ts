/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as FernDocsConfig from "../../../../api";
import * as core from "../../../../core";

export const WithAudience: core.serialization.ObjectSchema<serializers.WithAudience.Raw, FernDocsConfig.WithAudience> =
    core.serialization.object({
        audience: core.serialization.lazy(async () => (await import("../../..")).Audience).optional(),
    });

export declare namespace WithAudience {
    interface Raw {
        audience?: serializers.Audience.Raw | null;
    }
}
