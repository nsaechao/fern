import { z } from "zod";
import { AudiencesSchema } from "./AudiencesSchema";
import { WithDocsSchema } from "./WithDocsSchema";

export const SingleBaseUrlEnvironmentSchema = WithDocsSchema.extend({
    url: z.string(),
    audiences: z.optional(AudiencesSchema),
});

export type SingleBaseUrlEnvironmentSchema = z.infer<typeof SingleBaseUrlEnvironmentSchema>;
