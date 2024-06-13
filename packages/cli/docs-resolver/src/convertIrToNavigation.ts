import { docsYml } from "@fern-api/configuration";
import {
    convertAPIDefinitionToDb,
    convertDbAPIDefinitionToRead,
    DocsV1Write,
    FernNavigation,
    SDKSnippetHolder,
    visitDiscriminatedUnion
} from "@fern-api/fdr-sdk/dist";
import { AbsoluteFilePath, dirname, relative } from "@fern-api/fs-utils";
import { FernIr, IntermediateRepresentation } from "@fern-api/ir-sdk";
import { kebabCase } from "lodash-es";

const EMPTY_SNIPPETS_CONFIG = { snippets: [] };
const EMPTY_SNIPPET_HOLDER = new SDKSnippetHolder({
    snippetsBySdkId: {},
    snippetsConfigWithSdkId: {},
    snippetTemplatesByEndpoint: {},
    snippetsBySdkIdAndEndpointId: {},
    snippetTemplatesByEndpointId: {}
});

export async function convertIrToNavigation(
    ir: IntermediateRepresentation,
    apiDefinitionId: string,
    absoluteFilepathToDocsConfig: AbsoluteFilePath,
    fullSlugs: Map<AbsoluteFilePath, string>,
    navigation: docsYml.ParsedApiNavigationItem[]
): Promise<FernNavigation.ApiPackageChild[]> {
    // the navigation constructor doesn't need to know about snippets, so we can pass an empty object
    const api = convertDbAPIDefinitionToRead(
        convertAPIDefinitionToDb(
            convertIrToFdrApi({ ir, snippetsConfig: EMPTY_SNIPPETS_CONFIG }),
            apiDefinitionId,
            EMPTY_SNIPPET_HOLDER
        )
    );
    const holder = FernNavigation.ApiDefinitionHolder.create(api);

    // const items = visitAndSortNavigationSchema(
    //     navigation,
    //     defaultRoot.items,
    //     ir,
    //     absoluteFilepathToDocsConfig,
    //     fullSlugs
    // );

    // return {
    //     items,
    //     summaryPageId:
    //         rootSummaryAbsolutePath == null
    //             ? undefined
    //             : relative(dirname(absoluteFilepathToDocsConfig), rootSummaryAbsolutePath)
    // };
    return navigation.map((item) => convertParsedNavigationItem(item, holder, ir));
}

const ids = new Set<string>();
function nodeId(id: string): FernNavigation.NodeId {
    if (!ids.has(id)) {
        ids.add(id);
        return FernNavigation.NodeId(id);
    }
    let i = 0;
    while (ids.has(`${id}-${i}`)) {
        i++;
    }
    ids.add(`${id}-${i}`);
    return FernNavigation.NodeId(`${id}-${i}`);
}

function convertParsedNavigationItem(
    item: docsYml.ParsedApiNavigationItem,
    holder: FernNavigation.ApiDefinitionHolder,
    ir: IntermediateRepresentation,
    parentSlug: string,
    absoluteFilepathToDocsConfig: AbsoluteFilePath
): FernNavigation.ApiPackageChild {
    return visitDiscriminatedUnion(item)._visit<FernNavigation.ApiPackageChild>({
        item: (item) => {
            if (holder.api.subpackages[item.value] != null) {
                const subpackage = holder.api.subpackages[item.value]!;
                return {
                    id: nodeId(`${holder.api.id}:subpackage:${kebabCase(subpackage.name)}`),
                    type: "apiPackage",
                    title: subpackage.displayName ?? subpackage.name,
                    icon: undefined,
                    hidden: undefined,
                    overviewPageId: undefined,
                    slug: FernNavigation.Slug(FernNavigation.utils.slugjoin(parentSlug, subpackage.urlSlug)),
                    availability: undefined,
                    pointsTo: undefined,
                    children: subpackage.contents.map((item) =>
                        convertParsedNavigationItem(item, holder, ir, parentSlug, absoluteFilepathToDocsConfig)
                    )
                };
            }
        },
        page: (page) => ({
            id: nodeId(`${holder.api.id}:page:${kebabCase(page.title)}`),
            type: "page",
            title: page.title,
            icon: page.icon,
            hidden: page.hidden,
            slug: FernNavigation.Slug(FernNavigation.utils.slugjoin(parentSlug, page.slug ?? kebabCase(page.title))),
            pageId: FernNavigation.PageId(relative(dirname(absoluteFilepathToDocsConfig), page.absolutePath))
        }),
        link: (link) => ({
            id: nodeId(`${holder.api.id}:link:${kebabCase(link.text)}`),
            type: "link",
            title: link.text,
            icon: undefined,
            url: FernNavigation.Url(link.url)
        }),
        package: (pkg) => {
            const subpackage = holder.api.subpackages[pkg.package];
            const title = pkg.titleOverride ?? subpackage?.displayName ?? subpackage?.name ?? pkg.package;
            const slug = pkg.skipUrlSlug
                ? parentSlug
                : FernNavigation.utils.slugjoin(parentSlug, pkg.slug ?? kebabCase(title));
            return {
                id: nodeId(`${holder.api.id}:package:${kebabCase(pkg.package)}`),
                apiDefinitionId: FernNavigation.ApiDefinitionId(holder.api.id),
                type: "apiPackage",
                title,
                icon: pkg.icon,
                hidden: pkg.hidden,
                overviewPageId:
                    pkg.summaryAbsolutePath != null
                        ? FernNavigation.PageId(
                              relative(dirname(absoluteFilepathToDocsConfig), pkg.summaryAbsolutePath)
                          )
                        : undefined,
                slug: FernNavigation.Slug(slug),
                availability: undefined,
                pointsTo: undefined,
                children: pkg.contents.map((item) =>
                    convertParsedNavigationItem(item, holder, ir, parentSlug, absoluteFilepathToDocsConfig)
                )
            };
        }
    });
}

export function convertIrToDefaultNavigationConfigRoot(
    ir: IntermediateRepresentation
): DocsV1Write.ApiNavigationConfigRoot {
    const items: DocsV1Write.ApiNavigationConfigItem[] = convertPackageToNavigationConfigItems(ir.rootPackage, ir);
    return { items };
}

interface Holder {
    endpointsByOriginalName: Map<string, FernIr.HttpEndpoint>;
    webhooksByOriginalName: Map<string, FernIr.Webhook>;
    webSocketsByOriginalName: Map<string, FernIr.WebSocketChannel>;
    endpoints: Map<FernNavigation.EndpointId, FernIr.HttpEndpoint>;
    webhooks: Map<FernNavigation.WebhookId, FernIr.Webhook>;
    webSockets: Map<FernNavigation.WebSocketId, FernIr.WebSocketChannel>;
}

function convertPackageToNavigationConfigItems(
    package_: FernIr.Package,
    ir: IntermediateRepresentation
): DocsV1Write.ApiNavigationConfigItem[] {
    if (package_.navigationConfig != null) {
        const pointsToPackage = ir.subpackages[package_.navigationConfig.pointsTo];
        if (pointsToPackage != null) {
            return convertPackageToNavigationConfigItems(pointsToPackage, ir);
        }
    }

    const items: DocsV1Write.ApiNavigationConfigItem[] = [];

    if (package_.service != null) {
        const httpService = ir.services[package_.service];

        httpService?.endpoints.forEach((endpoint) => {
            items.push({ type: "endpointId", value: endpoint.name.originalName });
        });
    }

    if (package_.websocket != null) {
        const channel = ir.websocketChannels?.[package_.websocket];
        if (channel != null) {
            items.push({ type: "websocketId", value: channel.name.originalName });
        }
    }

    if (package_.webhooks != null) {
        const webhooks = ir.webhookGroups[package_.webhooks];

        webhooks?.forEach((webhook) => {
            items.push({ type: "webhookId", value: webhook.name.originalName });
        });
    }

    package_.subpackages.forEach((subpackageId) => {
        const subpackage = ir.subpackages[subpackageId];

        if (subpackage != null) {
            items.push({
                type: "subpackage",
                subpackageId,
                items: convertPackageToNavigationConfigItems(subpackage, ir)
            });
        }
    });

    return items;
}

function createItemMatcher(key: string, ir: IntermediateRepresentation) {
    return function (item: DocsV1Write.ApiNavigationConfigItem): boolean {
        if (item.type === "subpackage") {
            // subpackages are keyed by a generated ID, so we need to look up the original name
            return ir.subpackages[item.subpackageId]?.name.originalName === key;
        } else if (item.type === "page") {
            return false;
        } else {
            // endpoints, webhooks, and websockets are keyed by their original name
            return key === item.value;
        }
    };
}

function visitAndSortNavigationSchema(
    navigationItems: docsYml.ParsedApiNavigationItem[],
    defaultItems: DocsV1Write.ApiNavigationConfigItem[],
    ir: IntermediateRepresentation,
    absoluteFilepathToDocsConfig: AbsoluteFilePath,
    fullSlugs: Map<AbsoluteFilePath, string>
): DocsV1Write.ApiNavigationConfigItem[] {
    const items: DocsV1Write.ApiNavigationConfigItem[] = [];
    for (const navigationItem of navigationItems) {
        if (navigationItem.type === "item") {
            const foundItem = defaultItems.find(createItemMatcher(navigationItem.value, ir));

            if (foundItem != null && foundItem.type !== "subpackage") {
                items.push(foundItem);
            } else if (foundItem != null) {
                items.push({
                    type: "subpackage",
                    subpackageId: foundItem.subpackageId,
                    items: []
                });
            }
        } else if (navigationItem.type === "page") {
            items.push({
                type: "page",
                id: relative(dirname(absoluteFilepathToDocsConfig), navigationItem.absolutePath),
                title: navigationItem.title,
                icon: undefined,
                hidden: undefined,
                urlSlugOverride: navigationItem.slug,
                fullSlug: fullSlugs.get(navigationItem.absolutePath)?.split("/")
            });
        } else {
            // item must be a collection of subpackages
            const foundItem = defaultItems.find(createItemMatcher(navigationItem.subpackageId, ir));

            if (foundItem != null && foundItem.type === "subpackage") {
                items.push({
                    type: "subpackage",
                    subpackageId: foundItem.subpackageId,
                    summaryPageId:
                        navigationItem.summaryAbsolutePath == null
                            ? undefined
                            : relative(dirname(absoluteFilepathToDocsConfig), navigationItem.summaryAbsolutePath),
                    items: visitAndSortNavigationSchema(
                        navigationItem.items,
                        foundItem.items,
                        ir,
                        absoluteFilepathToDocsConfig,
                        fullSlugs
                    )
                });
            }
        }
    }

    return items;
}
function convertIrToFdrApi(arg0: {
    ir: FernIr.IntermediateRepresentation;
    snippetsConfig: { snippets: never[] };
}): import("@fern-api/fdr-sdk/dist/client/generated/api/resources/api/resources/v1/resources/register").ApiDefinition {
    throw new Error("Function not implemented.");
}
