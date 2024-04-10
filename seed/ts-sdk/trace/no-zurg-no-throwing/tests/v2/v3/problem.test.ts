/**
 * This file was auto-generated by Fern from our API Definition.
 */

import { SeedTraceClient } from "../../../src/Client";

const client = new SeedTraceClient({
    environment: process.env.TESTS_BASE_URL || "test",
    token: process.env.TESTS_AUTH || "test",
    xRandomHeader: process.env.TESTS_HEADER || "test",
});

function adaptResponse(response: unknown) {
    return JSON.parse(JSON.stringify(response, (_key, value) => (value instanceof Set ? [...value] : value)));
}

describe("Problem", () => {
    test("getLightweightProblems", async () => {
        const response = await client.v2.v3.problem.getLightweightProblems();
        if (response.ok) {
            expect(adaptResponse(response.body)).toEqual([
                {
                    problemId: "string",
                    problemName: "string",
                    problemVersion: 1,
                    variableTypes: new Set([{ type: "integerType" }]),
                },
            ]);
        } else {
            fail("Response was not ok");
        }
    });

    test("getProblems", async () => {
        const response = await client.v2.v3.problem.getProblems();
        if (response.ok) {
            expect(adaptResponse(response.body)).toEqual([
                {
                    problemId: "string",
                    problemDescription: {
                        boards: [{ "0": "s", "1": "t", "2": "r", "3": "i", "4": "n", "5": "g", type: "html" }],
                    },
                    problemName: "string",
                    problemVersion: 1,
                    supportedLanguages: new Set(["JAVA"]),
                    customFiles: { type: "basic" },
                    generatedFiles: {
                        generatedTestCaseFiles: {
                            JAVA: {
                                files: [
                                    { filename: "string", directory: "string", contents: "string", editable: true },
                                ],
                            },
                        },
                        generatedTemplateFiles: {
                            JAVA: {
                                files: [
                                    { filename: "string", directory: "string", contents: "string", editable: true },
                                ],
                            },
                        },
                        other: {
                            JAVA: {
                                files: [
                                    { filename: "string", directory: "string", contents: "string", editable: true },
                                ],
                            },
                        },
                    },
                    customTestCaseTemplates: [
                        {
                            templateId: "string",
                            name: "string",
                            implementation: {
                                description: {
                                    boards: [
                                        { "0": "s", "1": "t", "2": "r", "3": "i", "4": "n", "5": "g", type: "html" },
                                    ],
                                },
                                function: { type: "withActualResult" },
                            },
                        },
                    ],
                    testcases: [
                        {
                            metadata: { id: "string", name: "string", hidden: true },
                            implementation: {
                                "0": "s",
                                "1": "t",
                                "2": "r",
                                "3": "i",
                                "4": "n",
                                "5": "g",
                                type: "templateId",
                            },
                            arguments: { string: { type: "integerValue" } },
                            expects: { expectedStdout: "string" },
                        },
                    ],
                    isPublic: true,
                },
            ]);
        } else {
            fail("Response was not ok");
        }
    });

    test("getLatestProblem", async () => {
        const response = await client.v2.v3.problem.getLatestProblem("string");
        if (response.ok) {
            expect(adaptResponse(response.body)).toEqual({
                problemId: "string",
                problemDescription: {
                    boards: [{ "0": "s", "1": "t", "2": "r", "3": "i", "4": "n", "5": "g", type: "html" }],
                },
                problemName: "string",
                problemVersion: 1,
                supportedLanguages: new Set(["JAVA"]),
                customFiles: { type: "basic" },
                generatedFiles: {
                    generatedTestCaseFiles: {
                        JAVA: {
                            files: [{ filename: "string", directory: "string", contents: "string", editable: true }],
                        },
                    },
                    generatedTemplateFiles: {
                        JAVA: {
                            files: [{ filename: "string", directory: "string", contents: "string", editable: true }],
                        },
                    },
                    other: {
                        JAVA: {
                            files: [{ filename: "string", directory: "string", contents: "string", editable: true }],
                        },
                    },
                },
                customTestCaseTemplates: [
                    {
                        templateId: "string",
                        name: "string",
                        implementation: {
                            description: {
                                boards: [{ "0": "s", "1": "t", "2": "r", "3": "i", "4": "n", "5": "g", type: "html" }],
                            },
                            function: { type: "withActualResult" },
                        },
                    },
                ],
                testcases: [
                    {
                        metadata: { id: "string", name: "string", hidden: true },
                        implementation: {
                            "0": "s",
                            "1": "t",
                            "2": "r",
                            "3": "i",
                            "4": "n",
                            "5": "g",
                            type: "templateId",
                        },
                        arguments: { string: { type: "integerValue" } },
                        expects: { expectedStdout: "string" },
                    },
                ],
                isPublic: true,
            });
        } else {
            fail("Response was not ok");
        }
    });

    test("getProblemVersion", async () => {
        const response = await client.v2.v3.problem.getProblemVersion("string", 1);
        if (response.ok) {
            expect(adaptResponse(response.body)).toEqual({
                problemId: "string",
                problemDescription: {
                    boards: [{ "0": "s", "1": "t", "2": "r", "3": "i", "4": "n", "5": "g", type: "html" }],
                },
                problemName: "string",
                problemVersion: 1,
                supportedLanguages: new Set(["JAVA"]),
                customFiles: { type: "basic" },
                generatedFiles: {
                    generatedTestCaseFiles: {
                        JAVA: {
                            files: [{ filename: "string", directory: "string", contents: "string", editable: true }],
                        },
                    },
                    generatedTemplateFiles: {
                        JAVA: {
                            files: [{ filename: "string", directory: "string", contents: "string", editable: true }],
                        },
                    },
                    other: {
                        JAVA: {
                            files: [{ filename: "string", directory: "string", contents: "string", editable: true }],
                        },
                    },
                },
                customTestCaseTemplates: [
                    {
                        templateId: "string",
                        name: "string",
                        implementation: {
                            description: {
                                boards: [{ "0": "s", "1": "t", "2": "r", "3": "i", "4": "n", "5": "g", type: "html" }],
                            },
                            function: { type: "withActualResult" },
                        },
                    },
                ],
                testcases: [
                    {
                        metadata: { id: "string", name: "string", hidden: true },
                        implementation: {
                            "0": "s",
                            "1": "t",
                            "2": "r",
                            "3": "i",
                            "4": "n",
                            "5": "g",
                            type: "templateId",
                        },
                        arguments: { string: { type: "integerValue" } },
                        expects: { expectedStdout: "string" },
                    },
                ],
                isPublic: true,
            });
        } else {
            fail("Response was not ok");
        }
    });
});
