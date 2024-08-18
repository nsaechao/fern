/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../index";
import * as SeedApi from "../../api/index";
import * as core from "../../core";

export const FetchResponse: core.serialization.ObjectSchema<serializers.FetchResponse.Raw, SeedApi.FetchResponse> =
    core.serialization.object({
        columns: core.serialization
            .record(
                core.serialization.string(),
                core.serialization.lazyObject(() => serializers.Column)
            )
            .optional(),
        namespace: core.serialization.string().optional(),
        usage: core.serialization.lazyObject(() => serializers.Usage).optional(),
    });

export declare namespace FetchResponse {
    interface Raw {
        columns?: Record<string, serializers.Column.Raw> | null;
        namespace?: string | null;
        usage?: serializers.Usage.Raw | null;
    }
}
