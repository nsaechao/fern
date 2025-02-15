/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../../index";
import * as FernIr from "../../../../../../api/index";
import * as core from "../../../../../../core";
import { TypeId } from "../../../../commons/types/TypeId";
import { NamedType } from "../../types/types/NamedType";
import { EndpointId } from "../../../../commons/types/EndpointId";
import { Endpoint } from "../../endpoints/types/Endpoint";
import { NamedParameter } from "../../types/types/NamedParameter";

export const DynamicIntermediateRepresentation: core.serialization.ObjectSchema<
    serializers.dynamic.DynamicIntermediateRepresentation.Raw,
    FernIr.dynamic.DynamicIntermediateRepresentation
> = core.serialization.objectWithoutOptionalProperties({
    version: core.serialization.stringLiteral("1.0.0"),
    types: core.serialization.record(TypeId, NamedType),
    endpoints: core.serialization.record(EndpointId, Endpoint),
    headers: core.serialization.list(NamedParameter).optional(),
});

export declare namespace DynamicIntermediateRepresentation {
    interface Raw {
        version: "1.0.0";
        types: Record<TypeId.Raw, NamedType.Raw>;
        endpoints: Record<EndpointId.Raw, Endpoint.Raw>;
        headers?: NamedParameter.Raw[] | null;
    }
}
