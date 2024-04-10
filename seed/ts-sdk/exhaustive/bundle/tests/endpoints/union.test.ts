/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as Fiddle from "../../src/api";
import { FiddleClient } from "../../src/Client";

const client = new FiddleClient({
    environment: process.env.TESTS_BASE_URL || "test",
    token: process.env.TESTS_AUTH || "test",
});

function adaptResponse(response: unknown) {
    return JSON.parse(JSON.stringify(response, (_key, value) => (value instanceof Set ? [...value] : value)));
}

describe("Union", () => {
    test("getAndReturnUnion", async () => {
        const response = await client.endpoints.union.getAndReturnUnion(
            Fiddle.types.Animal.dog({
                name: "string",
                likesToWoof: true,
            })
        );
        if (response.ok) {
            expect(adaptResponse(response.body)).toEqual({ animal: "dog", name: "string", likesToWoof: true });
        } else {
            fail("Response was not ok");
        }
    });
});
