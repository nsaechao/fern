/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../../../../index";
import * as SeedTrace from "../../../../../../../../api/index";
import * as core from "../../../../../../../../core";

export const TestCaseTemplate: core.serialization.ObjectSchema<
    serializers.v2.v3.TestCaseTemplate.Raw,
    SeedTrace.v2.v3.TestCaseTemplate
> = core.serialization.object({
    templateId: core.serialization.lazy(() => serializers.v2.v3.TestCaseTemplateId),
    name: core.serialization.string(),
    implementation: core.serialization.lazyObject(() => serializers.v2.v3.TestCaseImplementation),
});

export declare namespace TestCaseTemplate {
    interface Raw {
        templateId: serializers.v2.v3.TestCaseTemplateId.Raw;
        name: string;
        implementation: serializers.v2.v3.TestCaseImplementation.Raw;
    }
}
