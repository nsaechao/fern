/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernDefinition from "../../../../api/index";
import * as core from "../../../../core";
import { UnionVariantTypeReference } from "./UnionVariantTypeReference";

export const UnionTypeReference: core.serialization.Schema<
    serializers.UnionTypeReference.Raw,
    FernDefinition.UnionTypeReference
> = core.serialization.undiscriminatedUnion([core.serialization.string(), UnionVariantTypeReference]);

export declare namespace UnionTypeReference {
    type Raw = string | UnionVariantTypeReference.Raw;
}
