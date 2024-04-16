/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as FernIr from "../../../../api";
import * as core from "../../../../core";

export const OauthRefreshEndpoint: core.serialization.ObjectSchema<
    serializers.OauthRefreshEndpoint.Raw,
    FernIr.OauthRefreshEndpoint
> = core.serialization.objectWithoutOptionalProperties({
    endpointReference: core.serialization.lazy(async () => (await import("../../..")).EndpointId),
    requestFields: core.serialization.lazyObject(async () => (await import("../../..")).OauthRefreshTokenFields),
    responseFields: core.serialization.lazyObject(async () => (await import("../../..")).OauthAccessTokenFields),
});

export declare namespace OauthRefreshEndpoint {
    interface Raw {
        endpointReference: serializers.EndpointId.Raw;
        requestFields: serializers.OauthRefreshTokenFields.Raw;
        responseFields: serializers.OauthAccessTokenFields.Raw;
    }
}
