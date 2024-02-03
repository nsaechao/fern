/**
 * This file was auto-generated by Fern from our API Definition.
 */
package com.seed.literalHeaders.resources.withnonliteralheaders;

import com.seed.literalHeaders.core.ApiError;
import com.seed.literalHeaders.core.ClientOptions;
import com.seed.literalHeaders.core.ObjectMappers;
import com.seed.literalHeaders.core.RequestOptions;
import com.seed.literalHeaders.resources.withnonliteralheaders.requests.WithNonLiteralHeadersRequest;
import java.io.IOException;
import okhttp3.Headers;
import okhttp3.HttpUrl;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class WithNonLiteralHeadersClient {
    protected final ClientOptions clientOptions;

    public WithNonLiteralHeadersClient(ClientOptions clientOptions) {
        this.clientOptions = clientOptions;
    }

    public void get(WithNonLiteralHeadersRequest request) {
        get(request, null);
    }

    public void get(WithNonLiteralHeadersRequest request, RequestOptions requestOptions) {
        HttpUrl httpUrl = HttpUrl.parse(this.clientOptions.environment().getUrl())
                .newBuilder()
                .addPathSegments("with-non-literal-headers")
                .build();
        Request.Builder _requestBuilder = new Request.Builder()
                .url(httpUrl)
                .method("POST", RequestBody.create("", null))
                .headers(Headers.of(clientOptions.headers(requestOptions)));
        _requestBuilder.addHeader("integer", Integer.toString(request.getInteger()));
        if (request.getMaybeInteger().isPresent()) {
            _requestBuilder.addHeader(
                    "maybeInteger", request.getMaybeInteger().get().toString());
        }
        _requestBuilder.addHeader("literalServiceHeader", request.getLiteralServiceHeader());
        _requestBuilder.addHeader(
                "trueServiceHeader", request.getTrueServiceHeader().toString());
        _requestBuilder.addHeader("nonLiteralEndpointHeader", request.getNonLiteralEndpointHeader());
        _requestBuilder.addHeader("literalEndpointHeader", request.getLiteralEndpointHeader());
        _requestBuilder.addHeader(
                "trueEndpointHeader", request.getTrueEndpointHeader().toString());
        Request okhttpRequest = _requestBuilder.build();
        try {
            Response response =
                    clientOptions.httpClient().newCall(okhttpRequest).execute();
            if (response.isSuccessful()) {
                return;
            }
            throw new ApiError(
                    response.code(),
                    ObjectMappers.JSON_MAPPER.readValue(response.body().string(), Object.class));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
