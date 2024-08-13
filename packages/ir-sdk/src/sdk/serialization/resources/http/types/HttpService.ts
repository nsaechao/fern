/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernIr from "../../../../api/index";
import * as core from "../../../../core";
import { Availability } from "../../commons/types/Availability";
import { DeclaredServiceName } from "./DeclaredServiceName";
import { HttpPath } from "./HttpPath";
import { HttpEndpoint } from "./HttpEndpoint";
import { HttpHeader } from "./HttpHeader";
import { PathParameter } from "./PathParameter";
import { Encoding } from "../../types/types/Encoding";
import { Transport } from "./Transport";

export const HttpService: core.serialization.ObjectSchema<serializers.HttpService.Raw, FernIr.HttpService> =
    core.serialization.objectWithoutOptionalProperties({
        availability: Availability.optional(),
        name: DeclaredServiceName,
        displayName: core.serialization.string().optional(),
        basePath: HttpPath,
        endpoints: core.serialization.list(HttpEndpoint),
        headers: core.serialization.list(HttpHeader),
        pathParameters: core.serialization.list(PathParameter),
        encoding: Encoding.optional(),
        transport: Transport.optional(),
    });

export declare namespace HttpService {
    interface Raw {
        availability?: Availability.Raw | null;
        name: DeclaredServiceName.Raw;
        displayName?: string | null;
        basePath: HttpPath.Raw;
        endpoints: HttpEndpoint.Raw[];
        headers: HttpHeader.Raw[];
        pathParameters: PathParameter.Raw[];
        encoding?: Encoding.Raw | null;
        transport?: Transport.Raw | null;
    }
}
