/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as SeedApi from "../index";

export interface QueryResponse {
    results?: SeedApi.QueryResult[];
    matches?: SeedApi.ScoredColumn[];
    namespace?: string;
    usage?: SeedApi.Usage;
}
