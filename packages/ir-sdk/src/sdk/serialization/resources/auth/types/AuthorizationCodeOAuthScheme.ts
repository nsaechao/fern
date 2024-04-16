/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as FernIr from "../../../../api";
import * as core from "../../../../core";

export const AuthorizationCodeOAuthScheme: core.serialization.ObjectSchema<
    serializers.AuthorizationCodeOAuthScheme.Raw,
    FernIr.AuthorizationCodeOAuthScheme
> = core.serialization
    .objectWithoutOptionalProperties({
        authorizationCodeEnvVar: core.serialization
            .lazy(async () => (await import("../../..")).EnvironmentVariable)
            .optional(),
        authorizationEndpoint: core.serialization.lazyObject(
            async () => (await import("../../..")).OauthAuthorizationEndpoint
        ),
        tokenEndpoint: core.serialization.lazyObject(async () => (await import("../../..")).OauthTokenEndpoint),
        refreshEndpoint: core.serialization
            .lazyObject(async () => (await import("../../..")).OauthRefreshEndpoint)
            .optional(),
    })
    .extend(core.serialization.lazyObject(async () => (await import("../../..")).BaseOAuthScheme));

export declare namespace AuthorizationCodeOAuthScheme {
    interface Raw extends serializers.BaseOAuthScheme.Raw {
        authorizationCodeEnvVar?: serializers.EnvironmentVariable.Raw | null;
        authorizationEndpoint: serializers.OauthAuthorizationEndpoint.Raw;
        tokenEndpoint: serializers.OauthTokenEndpoint.Raw;
        refreshEndpoint?: serializers.OauthRefreshEndpoint.Raw | null;
    }
}
