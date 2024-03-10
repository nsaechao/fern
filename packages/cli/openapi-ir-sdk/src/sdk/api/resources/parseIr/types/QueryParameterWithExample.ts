/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernOpenapiIr from "../../..";

export interface QueryParameterWithExample extends FernOpenapiIr.WithDescription {
    name: string;
    schema: FernOpenapiIr.SchemaWithExample;
    style: string | undefined;
    explode: boolean | undefined;
    /** Populated by `x-fern-parameter-name` on a parameter object. */
    parameterNameOverride: string | undefined;
}
