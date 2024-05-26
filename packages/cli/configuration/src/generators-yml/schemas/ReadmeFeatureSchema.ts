import { z } from "zod";
import { ReadmeFeatureObjectSchema } from "./ReadmeFeatureObjectSchema";

export const ReadmeFeatureSchema = z.union([
    z.string().describe("Endpoint name in 'POST /users' format"),
    ReadmeFeatureObjectSchema
]);

export type ReadmeFeatureSchema = z.infer<typeof ReadmeFeatureSchema>;
