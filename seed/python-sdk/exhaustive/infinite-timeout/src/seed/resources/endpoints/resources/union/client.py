# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import SyncClientWrapper, AsyncClientWrapper
from .....core.request_options import RequestOptions
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_dict import remove_none_from_dict
from ....types.resources.union.types.animal import Animal

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore
            
# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)
class UnionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
    def get_and_return_union(self, *, request: Animal, request_options: typing.Optional[RequestOptions] = None) -> Animal:
        """
        Parameters:
            - request: Animal.
            
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import SeedExhaustive
        from seed.resources.types import Animal_Dog
        client = SeedExhaustive(token="YOUR_TOKEN", base_url="https://yourhost.com/path/to/api", )
        client.endpoints.union.get_and_return_union(request=Animal_Dog(animal="dog", name="string", likes_to_woof=True, ), )
        """
        _response = self._client_wrapper.httpx_client.request("POST", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "union"), 
            params=jsonable_encoder(request_options.get('additional_query_parameters') if request_options is not None else None),
            json=jsonable_encoder(request) if request_options is None or request_options.get('additional_body_parameters') is None else {**jsonable_encoder(request), **(jsonable_encoder(remove_none_from_dict(request_options.get('additional_body_parameters', {}))))},
            headers=jsonable_encoder(remove_none_from_dict({**self._client_wrapper.get_headers(),**(request_options.get('additional_headers', {}) if request_options is not None else {}),},
            )),
            timeout=request_options.get('timeout_in_seconds') if request_options is not None and request_options.get('timeout_in_seconds') is not None else None,
            retries=0,
            max_retries=request_options.get('max_retries') if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Animal, _response.json())# type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
class AsyncUnionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
    async def get_and_return_union(self, *, request: Animal, request_options: typing.Optional[RequestOptions] = None) -> Animal:
        """
        Parameters:
            - request: Animal.
            
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import AsyncSeedExhaustive
        from seed.resources.types import Animal_Dog
        client = AsyncSeedExhaustive(token="YOUR_TOKEN", base_url="https://yourhost.com/path/to/api", )
        await client.endpoints.union.get_and_return_union(request=Animal_Dog(animal="dog", name="string", likes_to_woof=True, ), )
        """
        _response = await self._client_wrapper.httpx_client.request("POST", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "union"), 
            params=jsonable_encoder(request_options.get('additional_query_parameters') if request_options is not None else None),
            json=jsonable_encoder(request) if request_options is None or request_options.get('additional_body_parameters') is None else {**jsonable_encoder(request), **(jsonable_encoder(remove_none_from_dict(request_options.get('additional_body_parameters', {}))))},
            headers=jsonable_encoder(remove_none_from_dict({**self._client_wrapper.get_headers(),**(request_options.get('additional_headers', {}) if request_options is not None else {}),},
            )),
            timeout=request_options.get('timeout_in_seconds') if request_options is not None and request_options.get('timeout_in_seconds') is not None else None,
            retries=0,
            max_retries=request_options.get('max_retries') if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Animal, _response.json())# type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
