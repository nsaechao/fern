# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import SyncClientWrapper, AsyncClientWrapper
from .resources.payment.client import PaymentClient, AsyncPaymentClient


class SeedIdempotencyHeaders:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.
    
    Parameters:
        - base_url: str. The base url to use for requests from the client.
        
        - token: typing.Union[str, typing.Callable[[], str]].
        
        - timeout: typing.Optional[float]. The timeout to be used, in seconds, for requests by default the timeout is 60 seconds.
        
        - httpx_client: typing.Optional[httpx.Client]. The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.
    ---
    from seed.client import SeedIdempotencyHeaders
    client = SeedIdempotencyHeaders(token="YOUR_TOKEN", base_url="https://yourhost.com/path/to/api", )
    """
    def __init__(self, *, base_url: str, token: typing.Union[str, typing.Callable[[], str]], timeout: typing.Optional[float] = 60, httpx_client: typing.Optional[httpx.Client] = None):
        self._client_wrapper = SyncClientWrapper(base_url=base_url, token=token, httpx_client=httpx.Client(timeout=timeout) if httpx_client is None else httpx_client
        )
        self.payment = PaymentClient(client_wrapper=self._client_wrapper)
class AsyncSeedIdempotencyHeaders:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.
    
    Parameters:
        - base_url: str. The base url to use for requests from the client.
        
        - token: typing.Union[str, typing.Callable[[], str]].
        
        - timeout: typing.Optional[float]. The timeout to be used, in seconds, for requests by default the timeout is 60 seconds.
        
        - httpx_client: typing.Optional[httpx.AsyncClient]. The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.
    ---
    from seed.client import AsyncSeedIdempotencyHeaders
    client = AsyncSeedIdempotencyHeaders(token="YOUR_TOKEN", base_url="https://yourhost.com/path/to/api", )
    """
    def __init__(self, *, base_url: str, token: typing.Union[str, typing.Callable[[], str]], timeout: typing.Optional[float] = 60, httpx_client: typing.Optional[httpx.AsyncClient] = None):
        self._client_wrapper = AsyncClientWrapper(base_url=base_url, token=token, httpx_client=httpx.AsyncClient(timeout=timeout) if httpx_client is None else httpx_client
        )
        self.payment = AsyncPaymentClient(client_wrapper=self._client_wrapper)
