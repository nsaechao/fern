/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernIr from "../../../../api/index";
import * as core from "../../../../core";
import { Name } from "../../commons/types/Name";

export const EndpointName: core.serialization.ObjectSchema<serializers.EndpointName.Raw, FernIr.EndpointName> = Name;

export declare namespace EndpointName {
    type Raw = Name.Raw;
}
