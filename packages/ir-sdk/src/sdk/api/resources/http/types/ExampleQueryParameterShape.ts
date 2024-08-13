/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernIr from "../../../index";

export type ExampleQueryParameterShape =
    | FernIr.ExampleQueryParameterShape.Single
    | FernIr.ExampleQueryParameterShape.Exploded
    | FernIr.ExampleQueryParameterShape.CommaSeparated;

export declare namespace ExampleQueryParameterShape {
    interface Single extends _Utils {
        type: "single";
    }

    interface Exploded extends _Utils {
        type: "exploded";
    }

    interface CommaSeparated extends _Utils {
        type: "commaSeparated";
    }

    interface _Utils {
        _visit: <_Result>(visitor: FernIr.ExampleQueryParameterShape._Visitor<_Result>) => _Result;
    }

    interface _Visitor<_Result> {
        single: () => _Result;
        exploded: () => _Result;
        commaSeparated: () => _Result;
        _other: (value: { type: string }) => _Result;
    }
}

export const ExampleQueryParameterShape = {
    single: (): FernIr.ExampleQueryParameterShape.Single => {
        return {
            type: "single",
            _visit: function <_Result>(
                this: FernIr.ExampleQueryParameterShape.Single,
                visitor: FernIr.ExampleQueryParameterShape._Visitor<_Result>
            ) {
                return FernIr.ExampleQueryParameterShape._visit(this, visitor);
            },
        };
    },

    exploded: (): FernIr.ExampleQueryParameterShape.Exploded => {
        return {
            type: "exploded",
            _visit: function <_Result>(
                this: FernIr.ExampleQueryParameterShape.Exploded,
                visitor: FernIr.ExampleQueryParameterShape._Visitor<_Result>
            ) {
                return FernIr.ExampleQueryParameterShape._visit(this, visitor);
            },
        };
    },

    commaSeparated: (): FernIr.ExampleQueryParameterShape.CommaSeparated => {
        return {
            type: "commaSeparated",
            _visit: function <_Result>(
                this: FernIr.ExampleQueryParameterShape.CommaSeparated,
                visitor: FernIr.ExampleQueryParameterShape._Visitor<_Result>
            ) {
                return FernIr.ExampleQueryParameterShape._visit(this, visitor);
            },
        };
    },

    _visit: <_Result>(
        value: FernIr.ExampleQueryParameterShape,
        visitor: FernIr.ExampleQueryParameterShape._Visitor<_Result>
    ): _Result => {
        switch (value.type) {
            case "single":
                return visitor.single();
            case "exploded":
                return visitor.exploded();
            case "commaSeparated":
                return visitor.commaSeparated();
            default:
                return visitor._other(value as any);
        }
    },
} as const;
