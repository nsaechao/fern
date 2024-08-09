/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernDocsConfig from "../../..";

export interface LayoutConfig {
    /**
     * Sets the maximum width of the docs layout, including the sidebar and content.
     *
     * @default: 88rem (1408px)
     *
     * Valid options are:
     *
     * - `{number}rem`
     * - `{number}px`
     * - `full` (100% of the viewport width)
     */
    pageWidth?: string;
    /**
     * Sets the maximum width of the markdown article content.
     *
     * @default: 44rem (704px)
     *
     * Valid options are:
     *
     * - `{number}rem`
     * - `{number}px`
     */
    contentWidth?: string;
    /**
     * Sets the width of the sidebar in desktop mode
     *
     * @default: 18rem (288px)
     *
     * Valid options are:
     *
     * - `{number}rem`
     * - `{number}px`
     */
    sidebarWidth?: string;
    /**
     * Sets the height of the header
     *
     * @default: 4rem (64px)
     *
     * Valid options are:
     *
     * - `{number}rem`
     * - `{number}px`
     */
    headerHeight?: string;
    /**
     * Sets the placement of the searchbar
     *
     * @default: `sidebar`
     *
     * Note: this setting is ignored when `disable-header` is set to true.
     */
    searchbarPlacement?: FernDocsConfig.SearchbarPlacement;
    /**
     * Set the placement of the tabs
     *
     * @default: `sidebar`
     *
     * Note: this setting is ignored when `disable-header` is set to true.
     */
    tabsPlacement?: FernDocsConfig.TabsPlacement;
    /**
     * Set the alignment of the mardown content.
     *
     * @default: `center`
     *
     * Side effects:
     *
     * - When the alignment is set to `center`, the "On this page" (ToC) will be aligned to the right of the page.
     * - When the alignment is set to `left`, the content will be aligned next to the right of the markdown content.
     */
    contentAlignment?: FernDocsConfig.ContentAlignment;
    /**
     * If `header-position` is set to `fixed`, the header will be fixed to the top of the viewport.
     * If `header-position` is set to `absolute`, the header will be absolute and will scroll with the content.
     *
     * @default: `fixed`
     */
    headerPosition?: FernDocsConfig.HeaderPosition;
    /**
     * If `disable-header` is set to true, the header will not be rendered. Instead, the logo will be rendered as part of the sidebar,
     * and a 1px border will separate the sidebar from the content.
     */
    disableHeader?: boolean;
}
