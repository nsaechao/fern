import { z } from "zod";
import { ReadmeFeatureSchema } from "./ReadmeFeatureSchema";

export const ReadmeSchema = z.strictObject({
    organization: z.string().describe("The organization written in the README.md title format (e.g. FastAPI"),
    bannerLink: z.optional(z.string()),
    docsLink: z.optional(z.string()),
    features: z
        .optional(z.record(z.array(ReadmeFeatureSchema)))
        .describe("Specifies a list of endpoints associated with the feature")
});

export type ReadmeSchema = z.infer<typeof ReadmeSchema>;
