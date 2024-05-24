/**
 * This file was auto-generated by Fern from our API Definition.
 */

import express from "express";
import * as errors from "../../../../../../errors/index";
import * as serializers from "../../../../../../serialization/index";

export interface ServiceServiceMethods {
    check(
        req: express.Request<
            {
                id: string;
            },
            never,
            never,
            never
        >,
        res: {
            send: () => Promise<void>;
            cookie: (cookie: string, value: string, options?: express.CookieOptions) => void;
            locals: any;
        },
        next: express.NextFunction
    ): void | Promise<void>;
    ping(
        req: express.Request<never, boolean, never, never>,
        res: {
            send: (responseBody: boolean) => Promise<void>;
            cookie: (cookie: string, value: string, options?: express.CookieOptions) => void;
            locals: any;
        },
        next: express.NextFunction
    ): void | Promise<void>;
}

export class ServiceService {
    private router;

    constructor(private readonly methods: ServiceServiceMethods, middleware: express.RequestHandler[] = []) {
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
        this.router.get("/check/:id", async (req, res, next) => {
            try {
                await this.methods.check(
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
                if (error instanceof errors.SeedExamplesError) {
                    console.warn(
                        `Endpoint 'check' unexpectedly threw ${error.constructor.name}.` +
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
        this.router.get("/ping", async (req, res, next) => {
            try {
                await this.methods.ping(
                    req as any,
                    {
                        send: async (responseBody) => {
                            res.json(
                                await serializers.health.service.ping.Response.jsonOrThrow(responseBody, {
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
                if (error instanceof errors.SeedExamplesError) {
                    console.warn(
                        `Endpoint 'ping' unexpectedly threw ${error.constructor.name}.` +
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
        return this.router;
    }
}
