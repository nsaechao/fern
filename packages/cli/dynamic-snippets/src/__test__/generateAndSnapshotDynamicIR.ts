import { Audiences } from "@fern-api/configuration";
import { AbsoluteFilePath, join, RelativeFilePath, stringifyLargeObject } from "@fern-api/fs-utils";
import { serialization as IrSerialization } from "@fern-api/ir-sdk";
import { createMockTaskContext } from "@fern-api/task-context";
import { AbstractAPIWorkspace } from "@fern-api/workspace-loader";
import { writeFile } from "fs/promises";
import { generateIntermediateRepresentation } from "@fern-api/ir-generator";
import { convertIrToDynamicSnippetsIr } from "../convertIrToDynamicSnippetsIr";

export async function generateAndSnapshotDynamicIR({
    workspace,
    workspaceName,
    audiences,
    absolutePathToIr
}: {
    workspace: AbstractAPIWorkspace<unknown>;
    workspaceName: string;
    absolutePathToIr: AbsoluteFilePath;
    audiences: Audiences;
}): Promise<void> {
    const context = createMockTaskContext();
    const fernWorkspace = await workspace.toFernWorkspace({
        context
    });

    const intermediateRepresentation = await generateIntermediateRepresentation({
        workspace: fernWorkspace,
        generationLanguage: undefined,
        audiences,
        keywords: undefined,
        smartCasing: true,
        disableExamples: false,
        readme: undefined,
        version: undefined,
        packageName: undefined,
        context
    });

    const dynamicIntermediateRepresentation = await convertIrToDynamicSnippetsIr(intermediateRepresentation);

    const dynamicIntermediateRepresentationJson = IrSerialization.dynamic.DynamicIntermediateRepresentation.jsonOrThrow(
        dynamicIntermediateRepresentation,
        {
            unrecognizedObjectKeys: "strip"
        }
    );

    await writeFile(
        join(AbsoluteFilePath.of(absolutePathToIr), RelativeFilePath.of(`${workspaceName}.json`)),
        await stringifyLargeObject(dynamicIntermediateRepresentationJson, { pretty: true })
    );
}
