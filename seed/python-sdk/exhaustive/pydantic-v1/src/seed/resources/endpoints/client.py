# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import SyncClientWrapper, AsyncClientWrapper
from .resources.enum.client import EnumClient, AsyncEnumClient
from .resources.union.client import UnionClient, AsyncUnionClient
from .resources.object.client import ObjectClient, AsyncObjectClient
from .resources.params.client import ParamsClient, AsyncParamsClient
from .resources.container.client import ContainerClient, AsyncContainerClient
from .resources.primitive.client import PrimitiveClient, AsyncPrimitiveClient
from .resources.http_methods.client import HttpMethodsClient, AsyncHttpMethodsClient


class EndpointsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.container = ContainerClient(client_wrapper=self._client_wrapper)
        self.enum = EnumClient(client_wrapper=self._client_wrapper)
        self.http_methods = HttpMethodsClient(client_wrapper=self._client_wrapper)
        self.object = ObjectClient(client_wrapper=self._client_wrapper)
        self.params = ParamsClient(client_wrapper=self._client_wrapper)
        self.primitive = PrimitiveClient(client_wrapper=self._client_wrapper)
        self.union = UnionClient(client_wrapper=self._client_wrapper)
class AsyncEndpointsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.container = AsyncContainerClient(client_wrapper=self._client_wrapper)
        self.enum = AsyncEnumClient(client_wrapper=self._client_wrapper)
        self.http_methods = AsyncHttpMethodsClient(client_wrapper=self._client_wrapper)
        self.object = AsyncObjectClient(client_wrapper=self._client_wrapper)
        self.params = AsyncParamsClient(client_wrapper=self._client_wrapper)
        self.primitive = AsyncPrimitiveClient(client_wrapper=self._client_wrapper)
        self.union = AsyncUnionClient(client_wrapper=self._client_wrapper)
