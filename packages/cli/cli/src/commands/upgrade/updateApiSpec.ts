import * as fs from "fs";
import { readFile, writeFile } from "fs/promises";
import yaml from "js-yaml";
import * as path from "path";
import { Readable } from "stream";
import { finished } from "stream/promises";
import { CliContext } from "../../cli-context/CliContext";
import { API_ORIGIN_LOCATION_KEY, ASYNC_API_LOCATION_KEY, OPENAPI_LOCATION_KEY } from "../fern-cli/schemas";
import { getFernDirectory, loadRawGeneratorsConfiguration } from "../fern-cli/utilities";

async function fetchAndWriteFile(url: string, path: string): Promise<void> {
    const resp = await fetch(url);
    if (resp.ok && resp.body) {
        console.debug("Origin successfully fetched, writing to file");
        // Write file to disk
        const fileStream = fs.createWriteStream(path);
        await finished(Readable.fromWeb(resp.body).pipe(fileStream));

        // Read and format file
        const fileContents = await readFile(path, "utf8");
        try {
            await writeFile(path, JSON.stringify(JSON.parse(fileContents), undefined, 2), "utf8");
        } catch (e) {
            await writeFile(path, yaml.dump(yaml.load(fileContents)), "utf8");
        }
        console.debug("File written successfully");
    }
}

export async function updateApiSpec({ cliContext, api }: { cliContext: CliContext; api: string }): Promise<void> {
    // Parse the generators config
    console.log("Loading generator configuration");
    const generatorConfig = await loadRawGeneratorsConfiguration(fullRepoPath);
    if (generatorConfig == null) {
        console.error(`Could not find generators config within repo: ${fullRepoPath}`);
        return;
    }

    // Fetch and update the API spec
    let origin;
    console.log("Checking for API spec to update");
    console.log(JSON.stringify(generatorConfig, null, 2));
    const fernDirectory = await getFernDirectory(fullRepoPath);
    if (generatorConfig.api != null) {
        let apis;
        if (generatorConfig.api instanceof Array) {
            apis = generatorConfig.api;
        } else {
            apis = [generatorConfig.api];
        }
        for (const api of apis) {
            if (typeof api !== "string" && api.origin != null) {
                console.log("Origin found, fetching spec from ", api.origin);
                origin = api.origin;
                await fetchAndWriteFile(api.origin, path.join(fernDirectory, api.path));
            }
        }
    } else if (generatorConfig[ASYNC_API_LOCATION_KEY] != null) {
        if (generatorConfig[API_ORIGIN_LOCATION_KEY] != null) {
            console.log("Origin found, fetching spec from ", generatorConfig[API_ORIGIN_LOCATION_KEY]);
            origin = generatorConfig[API_ORIGIN_LOCATION_KEY];
            await fetchAndWriteFile(
                generatorConfig[API_ORIGIN_LOCATION_KEY],
                path.join(fernDirectory, generatorConfig[ASYNC_API_LOCATION_KEY])
            );
        }
    } else if (generatorConfig[OPENAPI_LOCATION_KEY] != null) {
        const apiOrigin =
            typeof generatorConfig[OPENAPI_LOCATION_KEY] !== "string"
                ? generatorConfig[OPENAPI_LOCATION_KEY].origin ?? generatorConfig[API_ORIGIN_LOCATION_KEY]
                : generatorConfig[API_ORIGIN_LOCATION_KEY];

        const apiOutput =
            typeof generatorConfig[OPENAPI_LOCATION_KEY] !== "string"
                ? generatorConfig[OPENAPI_LOCATION_KEY].path
                : generatorConfig[OPENAPI_LOCATION_KEY];

        if (apiOrigin != null) {
            origin = apiOrigin;
            console.log("Origin found, fetching spec from ", apiOrigin);
            await fetchAndWriteFile(apiOrigin, path.join(fernDirectory, apiOutput));
        }
    }
}
