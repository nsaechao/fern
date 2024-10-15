/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernDefinition from "../../../../api/index";
import * as core from "../../../../core";
import { VariableDeclarationDetailed } from "./VariableDeclarationDetailed";

export const VariableDeclaration: core.serialization.Schema<
    serializers.VariableDeclaration.Raw,
    FernDefinition.VariableDeclaration
> = core.serialization.undiscriminatedUnion([core.serialization.string(), VariableDeclarationDetailed]);

export declare namespace VariableDeclaration {
    type Raw = string | VariableDeclarationDetailed.Raw;
}
