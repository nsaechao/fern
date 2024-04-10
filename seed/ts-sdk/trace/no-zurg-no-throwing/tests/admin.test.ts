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

describe("Admin", () => {
    test("updateTestSubmissionStatus", async () => {
        const response = await client.admin.updateTestSubmissionStatus("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32", {
            type: "stopped",
        });
        if (response.ok) {
            expect(response.body).toEqual(undefined);
        } else {
            fail("Response was not ok");
        }
    });

    test("sendTestSubmissionUpdate", async () => {
        const response = await client.admin.sendTestSubmissionUpdate("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32", {
            updateTime: new Date("2024-01-15T09:30:00.000Z"),
            updateInfo: {
                type: "running",
                value: SeedTrace.RunningSubmissionState.QueueingSubmission,
            },
        });
        if (response.ok) {
            expect(response.body).toEqual(undefined);
        } else {
            fail("Response was not ok");
        }
    });

    test("updateWorkspaceSubmissionStatus", async () => {
        const response = await client.admin.updateWorkspaceSubmissionStatus("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32", {
            type: "stopped",
        });
        if (response.ok) {
            expect(response.body).toEqual(undefined);
        } else {
            fail("Response was not ok");
        }
    });

    test("sendWorkspaceSubmissionUpdate", async () => {
        const response = await client.admin.sendWorkspaceSubmissionUpdate("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32", {
            updateTime: new Date("2024-01-15T09:30:00.000Z"),
            updateInfo: {
                type: "running",
                value: SeedTrace.RunningSubmissionState.QueueingSubmission,
            },
        });
        if (response.ok) {
            expect(response.body).toEqual(undefined);
        } else {
            fail("Response was not ok");
        }
    });

    test("storeTracedTestCase", async () => {
        const response = await client.admin.storeTracedTestCase("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32", "string", {
            result: {
                result: {
                    expectedResult: {
                        type: "integerValue",
                        value: 1,
                    },
                    actualResult: {
                        type: "value",
                        value: {
                            type: "integerValue",
                            value: 1,
                        },
                    },
                    passed: true,
                },
                stdout: "string",
            },
            traceResponses: [
                {
                    submissionId: "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    lineNumber: 1,
                    returnValue: {
                        type: "integerValue",
                        value: 1,
                    },
                    expressionLocation: {
                        start: 1,
                        offset: 1,
                    },
                    stack: {
                        numStackFrames: 1,
                        topStackFrame: {
                            methodName: "string",
                            lineNumber: 1,
                            scopes: [
                                {
                                    variables: {
                                        string: {
                                            type: "integerValue",
                                            value: 1,
                                        },
                                    },
                                },
                            ],
                        },
                    },
                    stdout: "string",
                },
            ],
        });
        if (response.ok) {
            expect(response.body).toEqual(undefined);
        } else {
            fail("Response was not ok");
        }
    });

    test("storeTracedTestCaseV2", async () => {
        const response = await client.admin.storeTracedTestCaseV2("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32", "string", [
            {
                submissionId: "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                lineNumber: 1,
                file: {
                    filename: "string",
                    directory: "string",
                },
                returnValue: {
                    type: "integerValue",
                    value: 1,
                },
                expressionLocation: {
                    start: 1,
                    offset: 1,
                },
                stack: {
                    numStackFrames: 1,
                    topStackFrame: {
                        methodName: "string",
                        lineNumber: 1,
                        scopes: [
                            {
                                variables: {
                                    string: {
                                        type: "integerValue",
                                        value: 1,
                                    },
                                },
                            },
                        ],
                    },
                },
                stdout: "string",
            },
        ]);
        if (response.ok) {
            expect(response.body).toEqual(undefined);
        } else {
            fail("Response was not ok");
        }
    });

    test("storeTracedWorkspace", async () => {
        const response = await client.admin.storeTracedWorkspace("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32", {
            workspaceRunDetails: {
                exceptionV2: {
                    type: "generic",
                },
                exception: {
                    exceptionType: "string",
                    exceptionMessage: "string",
                    exceptionStacktrace: "string",
                },
                stdout: "string",
            },
            traceResponses: [
                {
                    submissionId: "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    lineNumber: 1,
                    returnValue: {
                        type: "integerValue",
                        value: 1,
                    },
                    expressionLocation: {
                        start: 1,
                        offset: 1,
                    },
                    stack: {
                        numStackFrames: 1,
                        topStackFrame: {
                            methodName: "string",
                            lineNumber: 1,
                            scopes: [
                                {
                                    variables: {
                                        string: {
                                            type: "integerValue",
                                            value: 1,
                                        },
                                    },
                                },
                            ],
                        },
                    },
                    stdout: "string",
                },
            ],
        });
        if (response.ok) {
            expect(response.body).toEqual(undefined);
        } else {
            fail("Response was not ok");
        }
    });

    test("storeTracedWorkspaceV2", async () => {
        const response = await client.admin.storeTracedWorkspaceV2("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32", [
            {
                submissionId: "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                lineNumber: 1,
                file: {
                    filename: "string",
                    directory: "string",
                },
                returnValue: {
                    type: "integerValue",
                    value: 1,
                },
                expressionLocation: {
                    start: 1,
                    offset: 1,
                },
                stack: {
                    numStackFrames: 1,
                    topStackFrame: {
                        methodName: "string",
                        lineNumber: 1,
                        scopes: [
                            {
                                variables: {
                                    string: {
                                        type: "integerValue",
                                        value: 1,
                                    },
                                },
                            },
                        ],
                    },
                },
                stdout: "string",
            },
        ]);
        if (response.ok) {
            expect(response.body).toEqual(undefined);
        } else {
            fail("Response was not ok");
        }
    });
});
