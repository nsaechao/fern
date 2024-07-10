/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as SeedTrace from "../../../../api/index";
import * as core from "../../../../core";
import { ProblemDescription } from "./ProblemDescription";
import { ProblemFiles } from "./ProblemFiles";
import { Language } from "../../commons/types/Language";
import { VariableTypeAndName } from "./VariableTypeAndName";
import { TestCaseWithExpectedResult } from "../../commons/types/TestCaseWithExpectedResult";

export const CreateProblemRequest: core.serialization.ObjectSchema<
    serializers.CreateProblemRequest.Raw,
    SeedTrace.CreateProblemRequest
> = core.serialization.object({
    problemName: core.serialization.string(),
    problemDescription: ProblemDescription,
    files: core.serialization.record(Language, ProblemFiles.optional()),
    inputParams: core.serialization.list(VariableTypeAndName),
    outputType: core.serialization.lazy(() => serializers.VariableType),
    testcases: core.serialization.list(TestCaseWithExpectedResult),
    methodName: core.serialization.string(),
});

export declare namespace CreateProblemRequest {
    interface Raw {
        problemName: string;
        problemDescription: ProblemDescription.Raw;
        files: Record<Language.Raw, ProblemFiles.Raw | null | undefined>;
        inputParams: VariableTypeAndName.Raw[];
        outputType: serializers.VariableType.Raw;
        testcases: TestCaseWithExpectedResult.Raw[];
        methodName: string;
    }
}
