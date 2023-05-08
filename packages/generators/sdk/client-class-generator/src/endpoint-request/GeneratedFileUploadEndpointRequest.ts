import { FileProperty, HttpEndpoint, HttpRequestBody, HttpService } from "@fern-fern/ir-model/http";
import { Fetcher, getTextOfTsNode, PackageId } from "@fern-typescript/commons";
import { SdkClientClassContext } from "@fern-typescript/contexts";
import { OptionalKind, ParameterDeclarationStructure, ts } from "ts-morph";
import { appendPropertyToFormData } from "../endpoints/utils/appendPropertyToFormData";
import { GeneratedQueryParams } from "../endpoints/utils/GeneratedQueryParams";
import { generateHeaders } from "../endpoints/utils/generateHeaders";
import { getParameterNameForFile } from "../endpoints/utils/getParameterNameForFile";
import { getParameterNameForPathParameter } from "../endpoints/utils/getParameterNameForPathParameter";
import { getPathParametersForEndpointSignature } from "../endpoints/utils/getPathParametersForEndpointSignature";
import { GeneratedSdkClientClassImpl } from "../GeneratedSdkClientClassImpl";
import { FileUploadRequestParameter } from "../request-parameter/FileUploadRequestParameter";
import { GeneratedEndpointRequest } from "./GeneratedEndpointRequest";

export declare namespace GeneratedFileUploadEndpointRequest {
    export interface Init {
        packageId: PackageId;
        service: HttpService;
        endpoint: HttpEndpoint;
        requestBody: HttpRequestBody.FileUpload;
        generatedSdkClientClass: GeneratedSdkClientClassImpl;
    }
}

export class GeneratedFileUploadEndpointRequest implements GeneratedEndpointRequest {
    private static FORM_DATA_VARIABLE_NAME = "_request";

    private requestParameter: FileUploadRequestParameter | undefined;
    private queryParams: GeneratedQueryParams | undefined;
    private service: HttpService;
    private endpoint: HttpEndpoint;
    private requestBody: HttpRequestBody.FileUpload;
    private generatedSdkClientClass: GeneratedSdkClientClassImpl;

    constructor({
        packageId,
        service,
        endpoint,
        requestBody,
        generatedSdkClientClass,
    }: GeneratedFileUploadEndpointRequest.Init) {
        this.service = service;
        this.endpoint = endpoint;
        this.requestBody = requestBody;
        this.generatedSdkClientClass = generatedSdkClientClass;

        if (requestBody.properties.some((property) => property.type === "bodyProperty")) {
            if (this.endpoint.sdkRequest == null) {
                throw new Error("SdkRequest is not defined for file upload endpoint");
            }
            if (this.endpoint.sdkRequest.shape.type != "wrapper") {
                throw new Error("SdkRequest is not a wrapper for file upload endpoint");
            }
            this.requestParameter = new FileUploadRequestParameter({
                packageId,
                service,
                endpoint,
                sdkRequest: this.endpoint.sdkRequest,
            });

            this.queryParams = new GeneratedQueryParams({
                requestParameter: this.requestParameter,
            });
        }
    }

    public getEndpointParameters(context: SdkClientClassContext): OptionalKind<ParameterDeclarationStructure>[] {
        const parameters: OptionalKind<ParameterDeclarationStructure>[] = [];
        for (const property of this.requestBody.properties) {
            if (property.type === "file") {
                parameters.push({
                    name: getParameterNameForFile(property),
                    type: getTextOfTsNode(this.getFileParameterType(property, context)),
                });
            }
        }
        for (const pathParameter of getPathParametersForEndpointSignature(this.service, this.endpoint)) {
            parameters.push({
                name: getParameterNameForPathParameter(pathParameter),
                type: getTextOfTsNode(context.type.getReferenceToType(pathParameter.valueType).typeNode),
            });
        }

        if (this.requestParameter != null) {
            parameters.push(this.requestParameter.getParameterDeclaration(context));
        }
        return parameters;
    }

    private getFileParameterType(property: FileProperty, context: SdkClientClassContext): ts.TypeNode {
        const types = [
            ts.factory.createTypeReferenceNode(ts.factory.createIdentifier("File")),
            context.base.externalDependencies.fs.ReadStream._getReferenceToType(),
        ];
        if (property.isOptional) {
            types.push(ts.factory.createKeywordTypeNode(ts.SyntaxKind.UndefinedKeyword));
        }
        return ts.factory.createUnionTypeNode(types);
    }

    public getBuildRequestStatements(context: SdkClientClassContext): ts.Statement[] {
        const statements: ts.Statement[] = [];

        if (this.requestParameter != null) {
            statements.push(...this.requestParameter.getInitialStatements());
        }

        if (this.queryParams != null) {
            statements.push(...this.queryParams.getBuildStatements(context));
        }

        statements.push(
            ts.factory.createVariableStatement(
                undefined,
                ts.factory.createVariableDeclarationList(
                    [
                        ts.factory.createVariableDeclaration(
                            GeneratedFileUploadEndpointRequest.FORM_DATA_VARIABLE_NAME,
                            undefined,
                            undefined,
                            context.base.externalDependencies.formData._instantiate()
                        ),
                    ],
                    ts.NodeFlags.Const
                )
            )
        );
        for (const property of this.requestBody.properties) {
            statements.push(
                appendPropertyToFormData({
                    property,
                    context,
                    referenceToFormData: ts.factory.createIdentifier(
                        GeneratedFileUploadEndpointRequest.FORM_DATA_VARIABLE_NAME
                    ),
                    requestParameter: this.requestParameter,
                })
            );
        }

        return statements;
    }

    public getFetcherRequestArgs(
        context: SdkClientClassContext
    ): Pick<Fetcher.Args, "headers" | "queryParameters" | "body" | "contentType"> {
        return {
            headers: this.getHeaders(context),
            queryParameters: this.queryParams != null ? this.queryParams.getReferenceTo(context) : undefined,
            body: ts.factory.createIdentifier(GeneratedFileUploadEndpointRequest.FORM_DATA_VARIABLE_NAME),
            contentType: ts.factory.createBinaryExpression(
                ts.factory.createStringLiteral("multipart/form-data; boundary="),
                ts.factory.createToken(ts.SyntaxKind.PlusToken),
                context.base.externalDependencies.formData.getBoundary({
                    referencetoFormData: ts.factory.createIdentifier(
                        GeneratedFileUploadEndpointRequest.FORM_DATA_VARIABLE_NAME
                    ),
                })
            ),
        };
    }

    private getHeaders(context: SdkClientClassContext): ts.ObjectLiteralElementLike[] {
        return generateHeaders({
            context,
            requestParameter: this.requestParameter,
            generatedSdkClientClass: this.generatedSdkClientClass,
            service: this.service,
            endpoint: this.endpoint,
            additionalHeaders: [
                {
                    header: "Content-Length",
                    value: context.base.coreUtilities.formDataUtils.getFormDataContentLength({
                        referenceToFormData: ts.factory.createIdentifier(
                            GeneratedFileUploadEndpointRequest.FORM_DATA_VARIABLE_NAME
                        ),
                    }),
                },
            ],
        });
    }

    public getReferenceToRequestBody(): ts.Expression | undefined {
        return this.requestParameter?.getReferenceToRequestBody();
    }

    public getReferenceToQueryParameter(queryParameterKey: string, context: SdkClientClassContext): ts.Expression {
        if (this.requestParameter == null) {
            throw new Error("Cannot get reference to query parameter because request parameter is not defined.");
        }
        return this.requestParameter.getReferenceToQueryParameter(queryParameterKey, context);
    }
}
