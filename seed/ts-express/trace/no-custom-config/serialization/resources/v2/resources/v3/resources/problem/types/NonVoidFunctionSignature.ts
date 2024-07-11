/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../../../../index";
import * as SeedTrace from "../../../../../../../../api/index";
import * as core from "../../../../../../../../core";

export const NonVoidFunctionSignature: core.serialization.ObjectSchema<
    serializers.v2.v3.NonVoidFunctionSignature.Raw,
    SeedTrace.v2.v3.NonVoidFunctionSignature
> = core.serialization.object({
    parameters: core.serialization.list(core.serialization.lazyObject(() => serializers.v2.v3.Parameter)),
    returnType: core.serialization.lazy(() => serializers.VariableType),
});

export declare namespace NonVoidFunctionSignature {
    interface Raw {
        parameters: serializers.v2.v3.Parameter.Raw[];
        returnType: serializers.VariableType.Raw;
    }
}
