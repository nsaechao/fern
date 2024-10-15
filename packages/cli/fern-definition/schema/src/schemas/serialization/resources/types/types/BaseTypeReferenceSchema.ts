/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernDefinition from "../../../../api/index";
import * as core from "../../../../core";
import { EncodingSchema } from "../../encoding/types/EncodingSchema";
import { ValidationSchema } from "../../validation/types/ValidationSchema";
import { WithDocsSchema } from "../../commons/types/WithDocsSchema";
import { WithAvailability } from "../../commons/types/WithAvailability";

export const BaseTypeReferenceSchema: core.serialization.ObjectSchema<
    serializers.BaseTypeReferenceSchema.Raw,
    FernDefinition.BaseTypeReferenceSchema
> = core.serialization
    .object({
        type: core.serialization.string(),
        default: core.serialization.unknown().optional(),
        encoding: EncodingSchema.optional(),
        validation: ValidationSchema.optional(),
    })
    .extend(WithDocsSchema)
    .extend(WithAvailability);

export declare namespace BaseTypeReferenceSchema {
    interface Raw extends WithDocsSchema.Raw, WithAvailability.Raw {
        type: string;
        default?: unknown | null;
        encoding?: EncodingSchema.Raw | null;
        validation?: ValidationSchema.Raw | null;
    }
}
