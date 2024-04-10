/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as SeedTrace from "../src/api";
import { SeedTraceClient } from "../src/Client";

const client = new SeedTraceClient({
    environment: process.env.TESTS_BASE_URL || "test",
    token: process.env.TESTS_AUTH || "test",
    xRandomHeader: process.env.TESTS_HEADER || "test",
});

describe("Playlist", () => {
    test("createPlaylist", async () => {
        const response = await client.playlist.createPlaylist(1, {
            datetime: new Date("2024-01-15T09:30:00.000Z"),
            optionalDatetime: new Date("2024-01-15T09:30:00.000Z"),
            body: {
                name: "string",
                problems: [SeedTrace.ProblemId("string")],
            },
        });
        if (response.ok) {
            expect(response.body).toEqual({
                playlistId: "string",
                ownerId: "string",
                name: "string",
                problems: ["string"],
            });
        } else {
            fail("Response was not ok");
        }
    });

    test("getPlaylists", async () => {
        const response = await client.playlist.getPlaylists(1, {
            limit: 1,
            otherField: "string",
            multiLineDocs: "string",
            optionalMultipleField: "string",
            multipleField: "string",
        });
        if (response.ok) {
            expect(response.body).toEqual([
                { playlistId: "string", ownerId: "string", name: "string", problems: ["string"] },
            ]);
        } else {
            fail("Response was not ok");
        }
    });

    test("getPlaylist", async () => {
        const response = await client.playlist.getPlaylist(1, SeedTrace.PlaylistId("string"));
        if (response.ok) {
            expect(response.body).toEqual({
                playlistId: "string",
                ownerId: "string",
                name: "string",
                problems: ["string"],
            });
        } else {
            fail("Response was not ok");
        }
    });

    test("updatePlaylist", async () => {
        const response = await client.playlist.updatePlaylist(1, SeedTrace.PlaylistId("string"), {
            name: "string",
            problems: [SeedTrace.ProblemId("string")],
        });
        if (response.ok) {
            expect(response.body).toEqual({
                playlistId: "string",
                ownerId: "string",
                name: "string",
                problems: ["string"],
            });
        } else {
            fail("Response was not ok");
        }
    });

    test("deletePlaylist", async () => {
        const response = await client.playlist.deletePlaylist(1, SeedTrace.PlaylistId("string"));
        if (response.ok) {
            expect(response.body).toEqual(undefined);
        } else {
            fail("Response was not ok");
        }
    });
});
