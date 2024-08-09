/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernOpenapiIr from "../../..";

export interface OAuthClientCredentials {
    clientIdEnvVar: string | undefined;
    clientSecretEnvVar: string | undefined;
    tokenPrefix: string | undefined;
    scopes: string[] | undefined;
    tokenEndpoint: FernOpenapiIr.OAuthTokenEndpoint;
    refreshEndpoint: FernOpenapiIr.OAuthRefreshEndpoint | undefined;
}
