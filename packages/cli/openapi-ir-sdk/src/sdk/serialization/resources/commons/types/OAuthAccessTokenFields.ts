/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as FernOpenapiIr from "../../../../api";
import * as core from "../../../../core";

export const OAuthAccessTokenFields: core.serialization.ObjectSchema<
    serializers.OAuthAccessTokenFields.Raw,
    FernOpenapiIr.OAuthAccessTokenFields
> = core.serialization.objectWithoutOptionalProperties({
    accessToken: core.serialization.string(),
    expiresIn: core.serialization.number().optional(),
    refreshToken: core.serialization.string().optional(),
});

export declare namespace OAuthAccessTokenFields {
    interface Raw {
        accessToken: string;
        expiresIn?: number | null;
        refreshToken?: string | null;
    }
}
