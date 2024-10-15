/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernDefinition from "../../../../api/index";
import * as core from "../../../../core";
import { OAuthGetTokenRequestProperties } from "./OAuthGetTokenRequestProperties";
import { OAuthGetTokenResponseProperties } from "./OAuthGetTokenResponseProperties";

export const OAuthGetTokenEndpoint: core.serialization.ObjectSchema<
    serializers.OAuthGetTokenEndpoint.Raw,
    FernDefinition.OAuthGetTokenEndpoint
> = core.serialization.object({
    endpoint: core.serialization.string(),
    requestProperties: core.serialization.property("request-properties", OAuthGetTokenRequestProperties.optional()),
    responseProperties: core.serialization.property("response-properties", OAuthGetTokenResponseProperties.optional()),
});

export declare namespace OAuthGetTokenEndpoint {
    interface Raw {
        endpoint: string;
        "request-properties"?: OAuthGetTokenRequestProperties.Raw | null;
        "response-properties"?: OAuthGetTokenResponseProperties.Raw | null;
    }
}
