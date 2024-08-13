/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernOpenapiIr from "../../../../api/index";
import * as core from "../../../../core";
import { TagId } from "./TagId";
import { WithDescription } from "./WithDescription";

export const Tag: core.serialization.ObjectSchema<serializers.Tag.Raw, FernOpenapiIr.Tag> = core.serialization
    .objectWithoutOptionalProperties({
        id: TagId,
    })
    .extend(WithDescription);

export declare namespace Tag {
    interface Raw extends WithDescription.Raw {
        id: TagId.Raw;
    }
}
