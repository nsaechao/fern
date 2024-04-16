import { Values } from "@fern-api/core-utils";
import { TypedExtensionId } from "./id";

export const FernOpenAPIExtension = {
    SDK_METHOD_NAME: TypedExtensionId.of<string>("x-fern-sdk-method-name"),
    SDK_GROUP_NAME: TypedExtensionId.of<string | string[]>("x-fern-sdk-group-name"),

    REQUEST_NAME_V1: "x-request-name",
    REQUEST_NAME_V2: "x-fern-request-name",
    TYPE_NAME: "x-fern-type-name",
    BOOLEAN_LITERAL: "x-fern-boolean-literal",

    SERVER_NAME_V1: "x-name",
    SERVER_NAME_V2: "x-fern-server-name",

    /**
     * Should align with the OpenAPI spec's `x-fern-sdk-group-name` extension.
     * This is a place where you can specify any display names related to the
     * configured SDK group names. These display names and descriptions will
     * come through in the docs.
     *
     * x-fern-groups:
     *  group1:
     *    display-name: Group 1
     *    description: This is group 1
     *    groups:
     *      group2 # add child groups
     */
    GROUPS: TypedExtensionId.of<string | string[]>("x-fern-groups"),

    /**
     * Filepath that contains any OpenAPI overrides
     * that you wan't Fern to add on top of your existing spec.
     *
     * x-fern-overrides-filepath: relative/path/to/file
     */
    OPENAPI_OVERIDES_FILEPATH: "x-fern-overrides-filepath",

    /**
     * Used to override the type with fern's type syntax
     * Bar:
     *  properties:
     *    createdDate:
     *      type: string
     *      x-fern-type: datetime
     *      x-fern-type:
     *        properties:
     *         a: string
     *         b: integer
     *      x-fern-type: optional<map<string, integer>>
     */
    TYPE_DEFINITION: "x-fern-type",

    /**
     * Used to specify if an endpoint should be generated
     * as a streaming endpoint.
     *
     * Example usage:
     *   paths:
     *     /path/to/my/endpoint:
     *       x-fern-streaming: true
     *
     * Alternatively, you can annotate the endpoint so that
     * it generates both a traditional unary endpoint,
     * as well as its streaming equivalent. The stream
     * condition property is included to specify a boolean
     * propetry that tells the server whether or not the
     * response should be streamed or not.
     *
     * Example usage:
     *   paths:
     *     /path/to/my/endpoint:
     *       x-fern-streaming:
     *         stream-condition: $request.stream
     *         response:
     *           $ref: ./path/to/response/type.yaml
     *         response-stream:
     *           $ref: ./path/to/response-stream/type.yaml
     */
    STREAMING: "x-fern-streaming",

    /**
     * Used to specify if an endpoint should be generated
     * as a paginated endpoint. Both cursor and offset pagination
     * examples are shown below.
     *
     * Example usage:
     *   paths:
     *     /path/to/my/endpoint:
     *       x-fern-pagination:
     *         cursor: $request.cursor
     *         next_cursor: $response.next
     *         results: $response.results
     *
     * Alternatively, if the configuration shown above is
     * specified at the document-level, paths can inherit the
     * configuration by setting the extension to true.
     *
     * Example usage:
     *   x-fern-pagination:
     *     offset: $request.page_number
     *     results: $response.results
     *
     *   paths:
     *     /path/to/my/endpoint:
     *       x-fern-pagination: true
     */
    PAGINATION: "x-fern-pagination",

    /**
     * Used to specify if an endpoint is actually
     * representing a webhook
     * Example usage:
     *   paths:
     *     /path/to/my/endpoint:
     *       x-fern-webhook: true
     */
    WEBHOOK: "x-fern-webhook",

    /**
     * Used to detect if an endpoint has an async version of it
     * Example usage:
     *   paths:
     *    /path/to/my/endpoint:
     *      x-fern-async-config:
     *        discriminant:
     *          type: header
     *          name: X-Header-Name
     *          value: async
     *        response-status-code: 202
     **/
    ASYNC_CONFIG: "x-fern-async-config",

    /**
     * Used to create veriables in the fern definition
     * Example usage:
     * x-fern-sdk-variables:
     *   appName:
     *     type: string
     * paths:
     *   /path/to/my/endpoint/{id}:
     *     parameters:
     *       - name: id
     *         in: path
     *         type: string
     *         x-fern-sdk-variable: appName
     */
    SDK_VARIABLES: "x-fern-sdk-variables",
    SDK_VARIABLE: "x-fern-sdk-variable",

    /**
     * Used to customize the name of the parameter used for a header.
     * Example usage:
     * paths:
     *   /path/to/my/endpoint/{id}:
     *     parameters:
     *       - in: header
     *         name: X-Fern-Version
     *         type: string
     *         x-fern-parameter-name: version
     */
    PARAMETER_NAME: "x-fern-parameter-name",

    /**
     * securitySchemes:
     *   Basic:
     *     scheme: http
     *     type: basic
     *     x-fern-username-variable-name: clientId
     *     x-fern-password-variable-name: clientSecret
     */
    BASIC_AUTH_USERNAME_VARIABLE_NAME: "x-fern-username-variable-name",
    BASIC_AUTH_PASSWORD_VARIABLE_NAME: "x-fern-password-variable-name",

    /**
     * securitySchemes:
     *   Bearer:
     *     scheme: http
     *     type: bearer
     *     x-fern-token-variable-name: apiKey
     */
    BEARER_TOKEN_VARIABLE_NAME: "x-fern-token-variable-name",

    /**
     * securitySchemes:
     *   Bearer:
     *     type: apiKey
     *     in: header
     *     name: X-API-KEY-ID
     *     x-fern-header-variable-name: apiKeyId
     */
    HEADER_VARIABLE_NAME: "x-fern-header-variable-name",

    /**
     * The x-fern-enum allows you to specify docs for the enum value.
     * If your enum is not codegen friendly (not alphanumeric), then you can specify a codegen name as well.
     *
     * MyEnum:
     *   enum:
     *     - VARIANT_ONE
     *     - VARIANT_TWO
     *   x-fern-enum:
     *     VARIANT_ONE:
     *       description: These are docs about the enum
     *       name: ONE
     */
    FERN_ENUM: "x-fern-enum",

    /**
     * Used to mark operations with audiences
     *
     * paths:
     *   /path/to/my/endpoint/{id}:
     *     x-fern-audiences:
     *       - external
     */
    AUDIENCES: "x-fern-audiences",

    /**
     * Used to tell fern to ignore endpoints.
     *
     * paths:
     *   /path/to/my/endpoint/{id}:
     *     get:
     *       x-fern-ignore: true
     */
    IGNORE: "x-fern-ignore",

    /**
     * paths:
     *  /path/to/my:
     *    get:
     *      x-fern-availability: ga # or beta, generally-available, deprecated,
     */
    AVAILABILITY: "x-fern-availability",

    /**
     * Used to signal that the SDK should return a specific property on the response.
     *
     * paths:
     *  /path/to/my:
     *    get:
     *      x-fern-sdk-return-value: data
     */
    RESPONSE_PROPERTY: "x-fern-sdk-return-value",

    /**
     * Used to resolve multiple schemas into a single schema. All the references
     * are replaced with a single schema.
     *
     * x-fern-resolutions:
     *  - name: User
     *    resolutions:
     *      - `#/components/schemas/Group/properties/user`
     *      - `#/components/schemas/User`
     */
    RESOLUTIONS: "x-fern-resolutions",

    /**
     * paths:
     *  /path/to/my:
     *    get:
     *     x-fern-fern-examples:
     *      - name: Example 1
     *        docs: This is an example
     *        request: {}
     *        response:
     *          body: {}
     *        code-samples:
     *          - language: typescript
     *            install: npm install my-client
     *            code: |
     *              import { MyClient } from "my-client";
     *              const client = new MyClient();
     *              const response = await client.myEndpoint();
     *              console.log(response);
     *            name: Console Log My Endpoint
     *            description: This is a code sample that logs the response
     */
    EXAMPLES: "x-fern-examples",

    /**
     * securitySchemes:
     *   Bearer:
     *     scheme: http
     *     type: bearer
     *     x-fern-bearer:
     *       name: apiKey
     *       env: MY_AUTH_TOKEN
     */
    FERN_BEARER_TOKEN: "x-fern-bearer",

    /**
     * securitySchemes:
     *   Bearer:
     *     type: apiKey
     *     in: header
     *     name: X-API-KEY-ID
     *     x-fern-header:
     *       name: header
     *       env: MY_AUTH_TOKEN
     */
    FERN_HEADER_AUTH: "x-fern-header",

    /**
     * securitySchemes:
     *   Basic:
     *     scheme: http
     *     type: basic
     *     x-fern-basic:
     *       username:
     *          name: username
     *          env: MY_USERNAME
     *       password:
     *          name: password
     *          env: MY_PASSWORD
     */
    FERN_BASIC_AUTH: "x-fern-basic",

    /**
     * If you are leveraging client credential grants, you must map out how
     * the response and request objects are mapped to general Oauth concepts (access_token, refresh_token, etc.)
     * see this in x-fern-oauth-token.token and x-fern-oauth-token.refresh
     *
     * securitySchemes:
     *   myOAuthSample:
     *     type: oauth2
     *     flows:
     *      authorizationCode:   # <---- OAuth flow(authorizationCode or clientCredentials)
     *          authorizationUrl: https://api.example.com/oauth2/authorize
     *          tokenUrl: https://api.example.com/oauth2/authorize
     *          refreshUrl: https://api.example.com/oauth2/authorize
     *          scopes:
     *              read_pets: read your pets
     *              write_pets: modify pets in your account
     *     x-fern-oauth:
     *       defaultScopes:      # <---- defaults to security.myOAuthSample
     *          - read_pets
     *       redirectUri: https://api.example.com/authed
     *       tokenPrefix: Token  # <---- defaults to Bearer
     *       clientIdEnv: MY_CLIENT_ID
     *       clientSecretEnv: MY_CLIENT_SECRET
     *       authorizationCodeEnv: MY_AUTH_CODE
     *
     *       # Optional configuration for authorization code flow
     *       authorizationCode:   # <---- The path to append to the base URL to get the authorization endpoint a user is meant to visit within the browser.
     *         path: /my/auth/path
     *         queryParams:
     *            - state
     *            - grant_type
     *       token:
     *          path: /my/token/path
     *          method: POST
     *          responseFields:
     *             accessToken: $response.token
     *             refreshToken: $response.refresh_token
     *             expiresIn: $response.expires_in
     *       refresh:
     *          path: /my/token/path
     *          method: POST
     *          requestFields:
     *             refreshToken: $request.query.token
     *          responseFields:
     *             accessToken: $response.token
     *             refreshToken: $response.refresh_token
     *             expiresIn: $response.expires_in
     *
     */
    FERN_OAUTH: "x-fern-oauth",

    /**
     * Allows users to specify which headers are global, and an optional alias for them
     * `header` is the name of the header used throughout your spec, while `name` is the
     * alias you'd like it to appear as within your generated SDK to the consumer.
     *
     * x-fern-global-headers:
     *  - header: our_api_key
     *    name: api_key
     *    optional: true
     *  - header: telemetry_id
     *    env: MY_ENVVAR
     *  - header: X-API-Version
     *    name: version
     *    type: literal<"2.10"> # The type of the header to use
     */
    FERN_GLOBAL_HEADERS: "x-fern-global-headers"
} as const;

export type FernOpenAPIExtension = Values<typeof FernOpenAPIExtension>;
