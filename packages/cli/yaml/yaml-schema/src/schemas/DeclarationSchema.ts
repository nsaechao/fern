import { z } from "zod";
import { AudiencesSchema } from "./AudiencesSchema";
import { AvailabilitySchema } from "./AvailabilitySchema";
import { AvailabilityStatusSchema } from "./AvailabilityStatusSchema";
import { WithDocsSchema } from "./WithDocsSchema";

export const DeclarationWithoutDocsSchema = z.strictObject({
    availability: z.optional(z.union([AvailabilityStatusSchema, AvailabilitySchema])),
    audiences: z.optional(AudiencesSchema)
});

export type DeclarationWithoutDocsSchema = z.infer<typeof DeclarationWithoutDocsSchema>;

export const DeclarationSchema = WithDocsSchema.extend(DeclarationWithoutDocsSchema.shape);

export type DeclarationSchema = z.infer<typeof DeclarationSchema>;
