import { z } from "zod";

export const AudiencesSchema = z.union([z.string(), z.array(z.string())]);

export type AudiencesSchema = z.infer<typeof AudiencesSchema>;
