/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernIr from "../../..";

export interface OauthRefreshEndpoint {
    /**
     * The refrence to the refresh token endpoint. This is specifically the endpoint ID without the `endpoint_` prefix.
     * This is gotten by following the path to the file the endpoint is defined in, so if the endpoint `refresh_token` is defined in foo/service.yml,
     * the endpoint ID would be `foo/service.refresh_token`.
     */
    endpointReference: FernIr.EndpointReference;
    requestFields: FernIr.OauthRefreshTokenFields;
    responseFields: FernIr.OauthAccessTokenFields;
}
