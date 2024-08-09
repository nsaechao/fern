/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as core from "../../../../core";
import * as SeedQueryParameters from "../../../index";
import urlJoin from "url-join";
import * as errors from "../../../../errors/index";

export declare namespace User {
    interface Options {
        environment: core.Supplier<string>;
    }

    interface RequestOptions {
        /** The maximum time to wait for a response in seconds. */
        timeoutInSeconds?: number;
        /** The number of times to retry the request. Defaults to 2. */
        maxRetries?: number;
        /** A hook to abort the request. */
        abortSignal?: AbortSignal;
    }
}

export class User {
    constructor(protected readonly _options: User.Options) {}

    /**
     * @param {SeedQueryParameters.GetUsersRequest} request
     * @param {User.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.user.getUsername({
     *         limit: 1,
     *         id: "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
     *         date: "2023-01-15",
     *         deadline: new Date("2024-01-15T09:30:00.000Z"),
     *         bytes: "SGVsbG8gd29ybGQh",
     *         user: {
     *             name: "string",
     *             tags: ["string"]
     *         },
     *         userList: [{
     *                 name: "string",
     *                 tags: ["string"]
     *             }],
     *         optionalDeadline: new Date("2024-01-15T09:30:00.000Z"),
     *         keyValue: {
     *             "string": "string"
     *         },
     *         optionalString: "string",
     *         nestedUser: {
     *             name: "string",
     *             user: {
     *                 name: "string",
     *                 tags: ["string"]
     *             }
     *         },
     *         optionalUser: {
     *             name: "string",
     *             tags: ["string"]
     *         },
     *         excludeUser: {
     *             name: "string",
     *             tags: ["string"]
     *         },
     *         filter: "string"
     *     })
     */
    public async getUsername(
        request: SeedQueryParameters.GetUsersRequest,
        requestOptions?: User.RequestOptions
    ): Promise<SeedQueryParameters.User> {
        const {
            limit,
            id,
            date,
            deadline,
            bytes,
            user,
            userList,
            optionalDeadline,
            keyValue,
            optionalString,
            nestedUser,
            optionalUser,
            excludeUser,
            filter,
        } = request;
        const _queryParams: Record<string, string | string[] | object | object[]> = {};
        _queryParams["limit"] = limit.toString();
        _queryParams["id"] = id;
        _queryParams["date"] = date;
        _queryParams["deadline"] = deadline;
        _queryParams["bytes"] = bytes;
        _queryParams["user"] = user;
        _queryParams["userList"] = JSON.stringify(userList);
        if (optionalDeadline != null) {
            _queryParams["optionalDeadline"] = optionalDeadline;
        }

        _queryParams["keyValue"] = JSON.stringify(keyValue);
        if (optionalString != null) {
            _queryParams["optionalString"] = optionalString;
        }

        _queryParams["nestedUser"] = nestedUser;
        if (optionalUser != null) {
            _queryParams["optionalUser"] = optionalUser;
        }

        if (Array.isArray(excludeUser)) {
            _queryParams["excludeUser"] = excludeUser.map((item) => item);
        } else {
            _queryParams["excludeUser"] = excludeUser;
        }

        if (Array.isArray(filter)) {
            _queryParams["filter"] = filter.map((item) => item);
        } else {
            _queryParams["filter"] = filter;
        }

        const _response = await core.fetcher({
            url: urlJoin(await core.Supplier.get(this._options.environment), "/user"),
            method: "GET",
            headers: {
                "X-Fern-Language": "JavaScript",
                "X-Fern-SDK-Name": "@fern/query-parameters",
                "X-Fern-SDK-Version": "0.0.1",
                "User-Agent": "@fern/query-parameters/0.0.1",
                "X-Fern-Runtime": core.RUNTIME.type,
                "X-Fern-Runtime-Version": core.RUNTIME.version,
            },
            contentType: "application/json",
            queryParameters: _queryParams,
            requestType: "json",
            timeoutMs: requestOptions?.timeoutInSeconds != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
            maxRetries: requestOptions?.maxRetries,
            abortSignal: requestOptions?.abortSignal,
        });
        if (_response.ok) {
            return _response.body as SeedQueryParameters.User;
        }

        if (_response.error.reason === "status-code") {
            throw new errors.SeedQueryParametersError({
                statusCode: _response.error.statusCode,
                body: _response.error.body,
            });
        }

        switch (_response.error.reason) {
            case "non-json":
                throw new errors.SeedQueryParametersError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.rawBody,
                });
            case "timeout":
                throw new errors.SeedQueryParametersTimeoutError();
            case "unknown":
                throw new errors.SeedQueryParametersError({
                    message: _response.error.errorMessage,
                });
        }
    }
}
