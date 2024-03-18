/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as environments from "../../../../environments";
import * as core from "../../../../core";
import * as SeedTrace from "../../..";
import { Problem } from "../resources/problem/client/Client";
import { V3 } from "../resources/v3/client/Client";

export declare namespace V2 {
    interface Options {
        environment?: core.Supplier<environments.SeedTraceEnvironment | string>;
        token?: core.Supplier<core.BearerToken | undefined>;
        xRandomHeader?: core.Supplier<string | undefined>;
    }

    interface RequestOptions {
        timeoutInSeconds?: number;
        maxRetries?: number;
    }
}

export class V2 {
    constructor(protected readonly _options: V2.Options = {}) {}

    public async test(requestOptions?: V2.RequestOptions): Promise<core.APIResponse<void, SeedTrace.v2.test.Error>> {
        const _response = await core.fetcher({
            url: (await core.Supplier.get(this._options.environment)) ?? environments.SeedTraceEnvironment.Prod,
            method: "GET",
            headers: {
                Authorization: await this._getAuthorizationHeader(),
                "X-Random-Header":
                    (await core.Supplier.get(this._options.xRandomHeader)) != null
                        ? await core.Supplier.get(this._options.xRandomHeader)
                        : undefined,
                "X-Fern-Language": "JavaScript",
                "X-Fern-SDK-Name": "@fern/trace",
                "X-Fern-SDK-Version": "0.0.1",
                "X-Fern-Runtime": core.RUNTIME.type,
                "X-Fern-Runtime-Version": core.RUNTIME.version,
            },
            contentType: "application/json",
            timeoutMs: requestOptions?.timeoutInSeconds != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
            maxRetries: requestOptions?.maxRetries,
        });
        if (_response.ok) {
            return {
                ok: true,
                body: undefined,
            };
        }

        return {
            ok: false,
            error: SeedTrace.v2.test.Error._unknown(_response.error),
        };
    }

    protected _problem: Problem | undefined;

    public get problem(): Problem {
        return (this._problem ??= new Problem(this._options));
    }

    protected _v3: V3 | undefined;

    public get v3(): V3 {
        return (this._v3 ??= new V3(this._options));
    }

    protected async _getAuthorizationHeader() {
        const bearer = await core.Supplier.get(this._options.token);
        if (bearer != null) {
            return `Bearer ${bearer}`;
        }

        return undefined;
    }
}
