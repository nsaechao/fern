/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernDocsConfig from "../../..";

export interface ApiSectionConfiguration {
    api: string;
    /** Name of API that we are referencing */
    apiName?: string;
    audiences?: string[];
    /** Defaults to false */
    displayErrors?: boolean;
    snippets?: FernDocsConfig.SnippetsConfiguration;
    /** Relative path to the markdown file. This summary is displayed at the top of the API section. */
    summary?: string;
    /** Advanced usage: when specified, this object will be used to customize the order that your API endpoints are displayed in the docs site, including subpackages, and additional markdown pages (to be rendered in between API endpoints). If not specified, the order will be inferred from the OpenAPI Spec or Fern Definition. */
    layout?: FernDocsConfig.ApiNavigationItems;
    icon?: string;
    hidden?: boolean;
    skipSlug?: boolean;
    /** If `scrolling` is set to `infinite`, you will be able to scroll between endpoints. If set to `paginated`, each endpoint will be self-contained, and you will need to click the next endpoint to view it. If not specified, the default is `infinite`. */
    scrolling?: FernDocsConfig.ApiScrollingConfiguration;
    /** If `unwrapped` is set to true, every endpoint will be viewable in the side-panel. Else, every endpoint will be default collapsed within each service. */
    unwrapped?: boolean;
}
