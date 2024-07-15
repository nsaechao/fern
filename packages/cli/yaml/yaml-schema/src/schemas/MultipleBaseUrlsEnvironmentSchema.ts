import { z } from "zod";
import { AudiencesSchema } from "./AudiencesSchema";
import { WithDocsSchema } from "./WithDocsSchema";

export const MultipleBaseUrlsEnvironmentSchema = WithDocsSchema.extend({
    urls: z.record(z.string()),
    audiences: z.optional(AudiencesSchema)
});

export type MultipleBaseUrlsEnvironmentSchema = z.infer<typeof MultipleBaseUrlsEnvironmentSchema>;
