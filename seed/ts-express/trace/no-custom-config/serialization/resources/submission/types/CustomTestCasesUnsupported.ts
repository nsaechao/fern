/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as SeedTrace from "../../../../api/index";
import * as core from "../../../../core";

export const CustomTestCasesUnsupported: core.serialization.ObjectSchema<
    serializers.CustomTestCasesUnsupported.Raw,
    SeedTrace.CustomTestCasesUnsupported
> = core.serialization.object({
    problemId: core.serialization.lazy(() => serializers.ProblemId),
    submissionId: core.serialization.lazy(() => serializers.SubmissionId),
});

export declare namespace CustomTestCasesUnsupported {
    interface Raw {
        problemId: serializers.ProblemId.Raw;
        submissionId: serializers.SubmissionId.Raw;
    }
}
