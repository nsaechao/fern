/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernOpenapiIr from "../../../../api/index";
import * as core from "../../../../core";

export const FileSchema: core.serialization.ObjectSchema<serializers.FileSchema.Raw, FernOpenapiIr.FileSchema> =
    core.serialization.objectWithoutOptionalProperties({
        isOptional: core.serialization.boolean(),
        isArray: core.serialization.boolean(),
    });

export declare namespace FileSchema {
    interface Raw {
        isOptional: boolean;
        isArray: boolean;
    }
}
