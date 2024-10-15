/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernDefinition from "../../../../api/index";
import * as core from "../../../../core";
import { WithAudiences } from "../../commons/types/WithAudiences";

export const SingleBaseUrlEnvironment: core.serialization.ObjectSchema<
    serializers.SingleBaseUrlEnvironment.Raw,
    FernDefinition.SingleBaseUrlEnvironment
> = core.serialization
    .object({
        url: core.serialization.string(),
    })
    .extend(WithAudiences);

export declare namespace SingleBaseUrlEnvironment {
    interface Raw extends WithAudiences.Raw {
        url: string;
    }
}
