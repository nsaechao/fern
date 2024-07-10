/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as SeedTrace from "../../../../api/index";
import * as core from "../../../../core";

export const StackInformation: core.serialization.ObjectSchema<
    serializers.StackInformation.Raw,
    SeedTrace.StackInformation
> = core.serialization.object({
    numStackFrames: core.serialization.number(),
    topStackFrame: core.serialization.lazyObject(() => serializers.StackFrame).optional(),
});

export declare namespace StackInformation {
    interface Raw {
        numStackFrames: number;
        topStackFrame?: serializers.StackFrame.Raw | null;
    }
}
