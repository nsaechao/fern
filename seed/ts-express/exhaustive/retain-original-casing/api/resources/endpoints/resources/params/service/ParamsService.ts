/**
 * This file was auto-generated by Fern from our API Definition.
 */

import express from "express";
import * as serializers from "../../../../../../serialization/index";
import * as errors from "../../../../../../errors/index";

export interface ParamsServiceMethods {
    getWithPath(
        req: express.Request<
            {
                param: string;
            },
            string,
            never,
            never
        >,
        res: {
            send: (responseBody: string) => Promise<void>;
            cookie: (cookie: string, value: string, options?: express.CookieOptions) => void;
            locals: any;
        },
        next: express.NextFunction
    ): void | Promise<void>;
    getWithQuery(
        req: express.Request<
            never,
            never,
            never,
            {
                query: string;
                number: number;
            }
        >,
        res: {
            send: () => Promise<void>;
            cookie: (cookie: string, value: string, options?: express.CookieOptions) => void;
            locals: any;
        },
        next: express.NextFunction
    ): void | Promise<void>;
    getWithAllowMultipleQuery(
        req: express.Request<
            never,
            never,
            never,
            {
                query: string;
                numer: number;
            }
        >,
        res: {
            send: () => Promise<void>;
            cookie: (cookie: string, value: string, options?: express.CookieOptions) => void;
            locals: any;
        },
        next: express.NextFunction
    ): void | Promise<void>;
    getWithPathAndQuery(
        req: express.Request<
            {
                param: string;
            },
            never,
            never,
            {
                query: string;
            }
        >,
        res: {
            send: () => Promise<void>;
            cookie: (cookie: string, value: string, options?: express.CookieOptions) => void;
            locals: any;
        },
        next: express.NextFunction
    ): void | Promise<void>;
    modifyWithPath(
        req: express.Request<
            {
                param: string;
            },
            string,
            string,
            never
        >,
        res: {
            send: (responseBody: string) => Promise<void>;
            cookie: (cookie: string, value: string, options?: express.CookieOptions) => void;
            locals: any;
        },
        next: express.NextFunction
    ): void | Promise<void>;
}

export class ParamsService {
    private router;

    constructor(private readonly methods: ParamsServiceMethods, middleware: express.RequestHandler[] = []) {
        this.router = express.Router({ mergeParams: true }).use(
            express.json({
                strict: false,
            }),
            ...middleware
        );
    }

    public addMiddleware(handler: express.RequestHandler): this {
        this.router.use(handler);
        return this;
    }

    public toRouter(): express.Router {
        this.router.get("/path/:param", async (req, res, next) => {
            try {
                await this.methods.getWithPath(
                    req as any,
                    {
                        send: async (responseBody) => {
                            res.json(
                                await serializers.endpoints.params.getWithPath.Response.jsonOrThrow(responseBody, {
                                    unrecognizedObjectKeys: "strip",
                                })
                            );
                        },
                        cookie: res.cookie.bind(res),
                        locals: res.locals,
                    },
                    next
                );
                next();
            } catch (error) {
                if (error instanceof errors.SeedExhaustiveError) {
                    console.warn(
                        `Endpoint 'getWithPath' unexpectedly threw ${error.constructor.name}.` +
                            ` If this was intentional, please add ${error.constructor.name} to` +
                            " the endpoint's errors list in your Fern Definition."
                    );
                    await error.send(res);
                } else {
                    res.status(500).json("Internal Server Error");
                }
                next(error);
            }
        });
        this.router.get("", async (req, res, next) => {
            try {
                await this.methods.getWithQuery(
                    req as any,
                    {
                        send: async () => {
                            res.sendStatus(204);
                        },
                        cookie: res.cookie.bind(res),
                        locals: res.locals,
                    },
                    next
                );
                next();
            } catch (error) {
                if (error instanceof errors.SeedExhaustiveError) {
                    console.warn(
                        `Endpoint 'getWithQuery' unexpectedly threw ${error.constructor.name}.` +
                            ` If this was intentional, please add ${error.constructor.name} to` +
                            " the endpoint's errors list in your Fern Definition."
                    );
                    await error.send(res);
                } else {
                    res.status(500).json("Internal Server Error");
                }
                next(error);
            }
        });
        this.router.get("", async (req, res, next) => {
            try {
                await this.methods.getWithAllowMultipleQuery(
                    req as any,
                    {
                        send: async () => {
                            res.sendStatus(204);
                        },
                        cookie: res.cookie.bind(res),
                        locals: res.locals,
                    },
                    next
                );
                next();
            } catch (error) {
                if (error instanceof errors.SeedExhaustiveError) {
                    console.warn(
                        `Endpoint 'getWithAllowMultipleQuery' unexpectedly threw ${error.constructor.name}.` +
                            ` If this was intentional, please add ${error.constructor.name} to` +
                            " the endpoint's errors list in your Fern Definition."
                    );
                    await error.send(res);
                } else {
                    res.status(500).json("Internal Server Error");
                }
                next(error);
            }
        });
        this.router.get("/path-query/:param", async (req, res, next) => {
            try {
                await this.methods.getWithPathAndQuery(
                    req as any,
                    {
                        send: async () => {
                            res.sendStatus(204);
                        },
                        cookie: res.cookie.bind(res),
                        locals: res.locals,
                    },
                    next
                );
                next();
            } catch (error) {
                if (error instanceof errors.SeedExhaustiveError) {
                    console.warn(
                        `Endpoint 'getWithPathAndQuery' unexpectedly threw ${error.constructor.name}.` +
                            ` If this was intentional, please add ${error.constructor.name} to` +
                            " the endpoint's errors list in your Fern Definition."
                    );
                    await error.send(res);
                } else {
                    res.status(500).json("Internal Server Error");
                }
                next(error);
            }
        });
        this.router.put("/path/:param", async (req, res, next) => {
            const request = await serializers.endpoints.params.modifyWithPath.Request.parse(req.body);
            if (request.ok) {
                req.body = request.value;
                try {
                    await this.methods.modifyWithPath(
                        req as any,
                        {
                            send: async (responseBody) => {
                                res.json(
                                    await serializers.endpoints.params.modifyWithPath.Response.jsonOrThrow(
                                        responseBody,
                                        { unrecognizedObjectKeys: "strip" }
                                    )
                                );
                            },
                            cookie: res.cookie.bind(res),
                            locals: res.locals,
                        },
                        next
                    );
                    next();
                } catch (error) {
                    if (error instanceof errors.SeedExhaustiveError) {
                        console.warn(
                            `Endpoint 'modifyWithPath' unexpectedly threw ${error.constructor.name}.` +
                                ` If this was intentional, please add ${error.constructor.name} to` +
                                " the endpoint's errors list in your Fern Definition."
                        );
                        await error.send(res);
                    } else {
                        res.status(500).json("Internal Server Error");
                    }
                    next(error);
                }
            } else {
                res.status(422).json({
                    errors: request.errors.map(
                        (error) => ["request", ...error.path].join(" -> ") + ": " + error.message
                    ),
                });
                next(request.errors);
            }
        });
        return this.router;
    }
}
