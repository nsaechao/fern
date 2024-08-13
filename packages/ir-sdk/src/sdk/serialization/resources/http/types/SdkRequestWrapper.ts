/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernIr from "../../../../api/index";
import * as core from "../../../../core";
import { Name } from "../../commons/types/Name";

export const SdkRequestWrapper: core.serialization.ObjectSchema<
    serializers.SdkRequestWrapper.Raw,
    FernIr.SdkRequestWrapper
> = core.serialization.objectWithoutOptionalProperties({
    wrapperName: Name,
    bodyKey: Name,
});

export declare namespace SdkRequestWrapper {
    interface Raw {
        wrapperName: Name.Raw;
        bodyKey: Name.Raw;
    }
}
