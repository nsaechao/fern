/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernOpenapiIr from "../../../../api/index";
import * as core from "../../../../core";
import { WithDescription } from "../../commons/types/WithDescription";
import { WithName } from "../../commons/types/WithName";
import { WithSdkGroupName } from "../../commons/types/WithSdkGroupName";
import { WithAvailability } from "../../commons/types/WithAvailability";
import { WithTitle } from "../../commons/types/WithTitle";

export const NullableSchema: core.serialization.ObjectSchema<
    serializers.NullableSchema.Raw,
    FernOpenapiIr.NullableSchema
> = core.serialization
    .objectWithoutOptionalProperties({
        value: core.serialization.lazy(() => serializers.Schema),
    })
    .extend(WithDescription)
    .extend(WithName)
    .extend(WithSdkGroupName)
    .extend(WithAvailability)
    .extend(WithTitle);

export declare namespace NullableSchema {
<<<<<<< HEAD
    interface Raw
        extends WithDescription.Raw,
            WithName.Raw,
            WithSchemaId.Raw,
            WithSdkGroupName.Raw,
            WithAvailability.Raw,
            WithTitle.Raw {
=======
    interface Raw extends WithDescription.Raw, WithName.Raw, WithSdkGroupName.Raw, WithAvailability.Raw {
>>>>>>> cafb0600e0 (not fully working)
        value: serializers.Schema.Raw;
    }
}
