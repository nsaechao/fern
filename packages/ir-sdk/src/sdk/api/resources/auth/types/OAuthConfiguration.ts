/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernIr from "../../..";

export type OAuthConfiguration =
    | FernIr.OAuthConfiguration.AuthorizationCode
    | FernIr.OAuthConfiguration.ClientCredentials;

export declare namespace OAuthConfiguration {
    interface AuthorizationCode extends FernIr.AuthorizationCodeOAuthScheme, _Utils {
        type: "authorizationCode";
    }

    interface ClientCredentials extends FernIr.ClientCredentialsOAuthScheme, _Utils {
        type: "clientCredentials";
    }

    interface _Utils {
        _visit: <_Result>(visitor: FernIr.OAuthConfiguration._Visitor<_Result>) => _Result;
    }

    interface _Visitor<_Result> {
        authorizationCode: (value: FernIr.AuthorizationCodeOAuthScheme) => _Result;
        clientCredentials: (value: FernIr.ClientCredentialsOAuthScheme) => _Result;
        _other: (value: { type: string }) => _Result;
    }
}

export const OAuthConfiguration = {
    authorizationCode: (value: FernIr.AuthorizationCodeOAuthScheme): FernIr.OAuthConfiguration.AuthorizationCode => {
        return {
            ...value,
            type: "authorizationCode",
            _visit: function <_Result>(
                this: FernIr.OAuthConfiguration.AuthorizationCode,
                visitor: FernIr.OAuthConfiguration._Visitor<_Result>
            ) {
                return FernIr.OAuthConfiguration._visit(this, visitor);
            },
        };
    },

    clientCredentials: (value: FernIr.ClientCredentialsOAuthScheme): FernIr.OAuthConfiguration.ClientCredentials => {
        return {
            ...value,
            type: "clientCredentials",
            _visit: function <_Result>(
                this: FernIr.OAuthConfiguration.ClientCredentials,
                visitor: FernIr.OAuthConfiguration._Visitor<_Result>
            ) {
                return FernIr.OAuthConfiguration._visit(this, visitor);
            },
        };
    },

    _visit: <_Result>(
        value: FernIr.OAuthConfiguration,
        visitor: FernIr.OAuthConfiguration._Visitor<_Result>
    ): _Result => {
        switch (value.type) {
            case "authorizationCode":
                return visitor.authorizationCode(value);
            case "clientCredentials":
                return visitor.clientCredentials(value);
            default:
                return visitor._other(value as any);
        }
    },
} as const;
