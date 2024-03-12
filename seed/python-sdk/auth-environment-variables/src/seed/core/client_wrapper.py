# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .http_client import HttpClient, AsyncHttpClient


class BaseClientWrapper:
    def __init__(self, *, x_another_header: str, api_key: str, base_url: str):
        self._x_another_header = x_another_header
        self.api_key = api_key
        self._base_url = base_url
    def get_headers(self) -> typing.Dict[str, str]:
        headers: typing.Dict[str, str]= {
        "X-Fern-Language": "Python",
        "X-Fern-SDK-Name": "seed",
        "X-Fern-SDK-Version": "0.0.0",
        }
        headers["X-Another-Header"] = self._x_another_header
        headers["X-FERN-API-KEY"] = self.api_key
        return headers
    def get_base_url(self) -> str:
        return self._base_url
class SyncClientWrapper(BaseClientWrapper):
    def __init__(self, *, x_another_header: str, api_key: str, base_url: str, httpx_client: httpx.Client):
        super().__init__(x_another_header=x_another_header, api_key=api_key, base_url=base_url)
        self.httpx_client = HttpClient(httpx_client=httpx_client)
class AsyncClientWrapper(BaseClientWrapper):
    def __init__(self, *, x_another_header: str, api_key: str, base_url: str, httpx_client: httpx.AsyncClient):
        super().__init__(x_another_header=x_another_header, api_key=api_key, base_url=base_url)
        self.httpx_client = AsyncHttpClient(httpx_client=httpx_client)
