/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernDefinition from "../../../../api/index";
import * as core from "../../../../core";
import { InlinedTypeDeclaration } from "./InlinedTypeDeclaration";

export const InlinedTypeDeclarationContainer: core.serialization.ObjectSchema<
    serializers.InlinedTypeDeclarationContainer.Raw,
    FernDefinition.InlinedTypeDeclarationContainer
> = core.serialization.object({
    type: InlinedTypeDeclaration,
});

export declare namespace InlinedTypeDeclarationContainer {
    interface Raw {
        type: InlinedTypeDeclaration.Raw;
    }
}
