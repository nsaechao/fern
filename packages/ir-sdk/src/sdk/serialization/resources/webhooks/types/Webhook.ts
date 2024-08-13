/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernIr from "../../../../api/index";
import * as core from "../../../../core";
import { WebhookId } from "../../commons/types/WebhookId";
import { WebhookName } from "./WebhookName";
import { WebhookHttpMethod } from "./WebhookHttpMethod";
import { HttpHeader } from "../../http/types/HttpHeader";
import { WebhookPayload } from "./WebhookPayload";
import { ExampleWebhookCall } from "./ExampleWebhookCall";
import { Declaration } from "../../commons/types/Declaration";

export const Webhook: core.serialization.ObjectSchema<serializers.Webhook.Raw, FernIr.Webhook> = core.serialization
    .objectWithoutOptionalProperties({
        id: WebhookId,
        name: WebhookName,
        displayName: core.serialization.string().optional(),
        method: WebhookHttpMethod,
        headers: core.serialization.list(HttpHeader),
        payload: WebhookPayload,
        examples: core.serialization.list(ExampleWebhookCall).optional(),
    })
    .extend(Declaration);

export declare namespace Webhook {
    interface Raw extends Declaration.Raw {
        id: WebhookId.Raw;
        name: WebhookName.Raw;
        displayName?: string | null;
        method: WebhookHttpMethod.Raw;
        headers: HttpHeader.Raw[];
        payload: WebhookPayload.Raw;
        examples?: ExampleWebhookCall.Raw[] | null;
    }
}
