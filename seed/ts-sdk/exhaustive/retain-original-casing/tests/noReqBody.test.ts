/**
 * This file was auto-generated by Fern from our API Definition.
 */

import { SeedExhaustiveClient } from "../src/Client";

const client = new SeedExhaustiveClient({
    environment: process.env.TESTS_BASE_URL || "test",
    token: process.env.TESTS_AUTH || "test",
});

describe("NoReqBody", () => {
    test("getWithNoRequestBody", async () => {
        const response = await client.noReqBody.getWithNoRequestBody();
        expect(response).toEqual(undefined);
    });

    test("postWithNoRequestBody", async () => {
        const response = await client.noReqBody.postWithNoRequestBody();
        expect(response).toEqual(undefined);
    });
});
