import path from "path";
import { AbsoluteFilePath } from "./AbsoluteFilePath";
import { RelativeFilePath } from "./RelativeFilePath";

export function getFilenameWithoutExtension(filepath: RelativeFilePath | AbsoluteFilePath): string {
    return path.parse(filepath).name;
}
