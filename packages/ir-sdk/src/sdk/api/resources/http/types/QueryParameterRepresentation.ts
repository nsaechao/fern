/**
 * This file was auto-generated by Fern from our API Definition.
 */

export type QueryParameterRepresentation = "EXPLODED" | "COMMA_DELIMITED" | "SPACE_DELIMITED" | "PIPE_DELIMITED";

export const QueryParameterRepresentation = {
    Exploded: "EXPLODED",
    CommaDelimited: "COMMA_DELIMITED",
    SpaceDelimited: "SPACE_DELIMITED",
    PipeDelimited: "PIPE_DELIMITED",
    _visit: <R>(value: QueryParameterRepresentation, visitor: QueryParameterRepresentation.Visitor<R>) => {
        switch (value) {
            case QueryParameterRepresentation.Exploded:
                return visitor.exploded();
            case QueryParameterRepresentation.CommaDelimited:
                return visitor.commaDelimited();
            case QueryParameterRepresentation.SpaceDelimited:
                return visitor.spaceDelimited();
            case QueryParameterRepresentation.PipeDelimited:
                return visitor.pipeDelimited();
            default:
                return visitor._other();
        }
    },
} as const;

export declare namespace QueryParameterRepresentation {
    interface Visitor<R> {
        exploded: () => R;
        commaDelimited: () => R;
        spaceDelimited: () => R;
        pipeDelimited: () => R;
        _other: () => R;
    }
}
