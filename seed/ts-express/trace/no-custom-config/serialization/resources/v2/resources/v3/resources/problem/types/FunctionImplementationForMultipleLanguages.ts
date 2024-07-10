/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../../../../index";
import * as SeedTrace from "../../../../../../../../api/index";
import * as core from "../../../../../../../../core";

export const FunctionImplementationForMultipleLanguages: core.serialization.ObjectSchema<
    serializers.v2.v3.FunctionImplementationForMultipleLanguages.Raw,
    SeedTrace.v2.v3.FunctionImplementationForMultipleLanguages
> = core.serialization.object({
    codeByLanguage: core.serialization.record(
        core.serialization.lazy(() => serializers.Language),
        core.serialization.lazyObject(() => serializers.v2.v3.FunctionImplementation).optional()
    ),
});

export declare namespace FunctionImplementationForMultipleLanguages {
    interface Raw {
        codeByLanguage: Record<
            serializers.Language.Raw,
            serializers.v2.v3.FunctionImplementation.Raw | null | undefined
        >;
    }
}
