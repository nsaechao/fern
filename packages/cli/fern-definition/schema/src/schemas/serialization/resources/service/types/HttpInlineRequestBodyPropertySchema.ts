/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernDefinition from "../../../../api/index";
import * as core from "../../../../core";
import { NonInlinedTypeReferenceSchemaWithContentType } from "./NonInlinedTypeReferenceSchemaWithContentType";
import { InlinedTypeReferenceSchemaWithContentType } from "./InlinedTypeReferenceSchemaWithContentType";
import { InlinedListTypeReferenceSchemaWithContentType } from "./InlinedListTypeReferenceSchemaWithContentType";

export const HttpInlineRequestBodyPropertySchema: core.serialization.Schema<
    serializers.HttpInlineRequestBodyPropertySchema.Raw,
    FernDefinition.HttpInlineRequestBodyPropertySchema
> = core.serialization.undiscriminatedUnion([
    core.serialization.string(),
    NonInlinedTypeReferenceSchemaWithContentType,
    InlinedTypeReferenceSchemaWithContentType,
    InlinedListTypeReferenceSchemaWithContentType,
]);

export declare namespace HttpInlineRequestBodyPropertySchema {
    type Raw =
        | string
        | NonInlinedTypeReferenceSchemaWithContentType.Raw
        | InlinedTypeReferenceSchemaWithContentType.Raw
        | InlinedListTypeReferenceSchemaWithContentType.Raw;
}
