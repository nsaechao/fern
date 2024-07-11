/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../../index";
import * as SeedExhaustive from "../../../../../../api/index";
import * as core from "../../../../../../core";

export const Request: core.serialization.Schema<
    serializers.endpoints.container.getAndReturnOptional.Request.Raw,
    SeedExhaustive.types.ObjectWithRequiredField | undefined
> = core.serialization.lazyObject(() => serializers.types.ObjectWithRequiredField).optional();

export declare namespace Request {
    type Raw = serializers.types.ObjectWithRequiredField.Raw | null | undefined;
}

export const Response: core.serialization.Schema<
    serializers.endpoints.container.getAndReturnOptional.Response.Raw,
    SeedExhaustive.types.ObjectWithRequiredField | undefined
> = core.serialization.lazyObject(() => serializers.types.ObjectWithRequiredField).optional();

export declare namespace Response {
    type Raw = serializers.types.ObjectWithRequiredField.Raw | null | undefined;
}
