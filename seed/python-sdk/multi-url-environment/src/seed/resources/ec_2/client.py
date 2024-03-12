# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import SyncClientWrapper, AsyncClientWrapper
from ...core.request_options import RequestOptions
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)
class Ec2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
    def boot_instance(self, *, size: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters:
            - size: str.
            
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import SeedMultiUrlEnvironment
        client = SeedMultiUrlEnvironment(token="YOUR_TOKEN", )
        client.ec_2.boot_instance(size="string", )
        """
        _response = self._client_wrapper.httpx_client.request("POST", urllib.parse.urljoin(f"{self._client_wrapper.get_environment().ec_2}/", "ec2/boot"), 
            params=jsonable_encoder(request_options.get('additional_query_parameters') if request_options is not None else None),
            json=jsonable_encoder({
                "size": size,
            }
            ) if request_options is None or request_options.get('additional_body_parameters') is None else {**jsonable_encoder({
                "size": size,
            }
            ), **(jsonable_encoder(remove_none_from_dict(request_options.get('additional_body_parameters', {}))))},
            headers=jsonable_encoder(remove_none_from_dict({**self._client_wrapper.get_headers(),**(request_options.get('additional_headers', {}) if request_options is not None else {}),},
            )),
            timeout=request_options.get('timeout_in_seconds') if request_options is not None and request_options.get('timeout_in_seconds') is not None else 60,
            retries=0,
            max_retries=request_options.get('max_retries') if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
class AsyncEc2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
    async def boot_instance(self, *, size: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters:
            - size: str.
            
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import AsyncSeedMultiUrlEnvironment
        client = AsyncSeedMultiUrlEnvironment(token="YOUR_TOKEN", )
        await client.ec_2.boot_instance(size="string", )
        """
        _response = await self._client_wrapper.httpx_client.request("POST", urllib.parse.urljoin(f"{self._client_wrapper.get_environment().ec_2}/", "ec2/boot"), 
            params=jsonable_encoder(request_options.get('additional_query_parameters') if request_options is not None else None),
            json=jsonable_encoder({
                "size": size,
            }
            ) if request_options is None or request_options.get('additional_body_parameters') is None else {**jsonable_encoder({
                "size": size,
            }
            ), **(jsonable_encoder(remove_none_from_dict(request_options.get('additional_body_parameters', {}))))},
            headers=jsonable_encoder(remove_none_from_dict({**self._client_wrapper.get_headers(),**(request_options.get('additional_headers', {}) if request_options is not None else {}),},
            )),
            timeout=request_options.get('timeout_in_seconds') if request_options is not None and request_options.get('timeout_in_seconds') is not None else 60,
            retries=0,
            max_retries=request_options.get('max_retries') if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
