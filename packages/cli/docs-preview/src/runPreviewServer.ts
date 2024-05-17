import { DocsV2Read } from "@fern-api/fdr-sdk";
import { TaskContext } from "@fern-api/task-context";
import { APIWorkspace, DocsWorkspace } from "@fern-api/workspace-loader";
import cors from "cors";
import express from "express";
import { watch } from "fs";
import http from "http";
import path from "path";
import { WebSocketServer, type WebSocket } from "ws";
import { getPreviewDocsDefinition } from "./previewDocs";

const PATH_TO_NEXT = "/Volumes/git/fern-platform/packages/ui/local-preview-bundle/out";

export async function runPreviewServer({
    docsWorkspace,
    apiWorkspaces,
    context
}: {
    docsWorkspace: DocsWorkspace;
    apiWorkspaces: APIWorkspace[];
    context: TaskContext;
}): Promise<void> {
    const app = express();
    const httpServer = http.createServer(app);
    const wss = new WebSocketServer({ server: httpServer });

    const connections = new Set<WebSocket>();

    wss.on("connection", function connection(ws) {
        connections.add(ws);

        ws.on("close", function close() {
            connections.delete(ws);
        });
    });

    app.use(cors());

    let docsDefinition = await getPreviewDocsDefinition({
        docsWorkspace,
        apiWorkspaces,
        context
    });

    let updates = 0;
    const opts = { recursive: true };
    watch(docsWorkspace.absoluteFilepath, opts, (_event, path) => {
        const lock = ++updates;
        context.logger.info(`File ${path} has been changed. Reloading...`);
        void getPreviewDocsDefinition({
            docsWorkspace,
            apiWorkspaces,
            context
        }).then((newDocsDefinition) => {
            if (lock !== updates) {
                return;
            }
            docsDefinition = newDocsDefinition;
            connections.forEach((ws) => {
                ws.send(JSON.stringify({ reload: true }));
            });
            context.logger.info("Docs reloaded");
        });
    });

    app.post("/v2/registry/docs/load-with-url", async (_, res) => {
        const response: DocsV2Read.LoadDocsForUrlResponse = {
            baseUrl: {
                domain: "localhost:3000",
                basePath: ""
            },
            definition: docsDefinition,
            lightModeEnabled: docsDefinition.config.colorsV3?.type !== "dark"
        };
        res.send(response);
    });

    app.get(/^\/_local\/(.*)/, (req, res) => {
        return res.sendFile(`/${req.params[0]}`);
    });

    app.get("/", (req, _res, next) => {
        if (req.headers.upgrade === "websocket") {
            return wss.handleUpgrade(req, req.socket, Buffer.alloc(0), (ws) => {
                wss.emit("connection", ws, req);
            });
        }
        return next();
    });

    app.use("/_next", express.static(path.join(PATH_TO_NEXT, "_next")));

    app.use("*", async (_req, res) => {
        return res.sendFile(path.join(PATH_TO_NEXT, "[[...slug]].html"));
    });

    app.listen(3000);

    context.logger.info("Running server on http://localhost:3000");

    // await infiinitely
    // eslint-disable-next-line @typescript-eslint/no-empty-function
    await new Promise(() => {});
}
