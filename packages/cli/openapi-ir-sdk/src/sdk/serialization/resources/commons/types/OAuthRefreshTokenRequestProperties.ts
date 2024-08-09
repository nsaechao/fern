/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as FernOpenapiIr from "../../../../api";
import * as core from "../../../../core";

export const OAuthRefreshTokenRequestProperties: core.serialization.ObjectSchema<
    serializers.OAuthRefreshTokenRequestProperties.Raw,
    FernOpenapiIr.OAuthRefreshTokenRequestProperties
> = core.serialization.objectWithoutOptionalProperties({
    refreshToken: core.serialization.string(),
});

export declare namespace OAuthRefreshTokenRequestProperties {
    interface Raw {
        refreshToken: string;
    }
}
