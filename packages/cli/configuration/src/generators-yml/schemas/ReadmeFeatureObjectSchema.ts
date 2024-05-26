import { z } from "zod";

export const ReadmeFeatureObjectSchema = z.strictObject({
    method: z.string(),
    path: z.string(),
    stream: z.optional(z.boolean())
});

export type ReadmeFeatureObjectSchema = z.infer<typeof ReadmeFeatureObjectSchema>;
