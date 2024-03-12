# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...types.operand import Operand
from ...core.api_error import ApiError
from ...core.client_wrapper import SyncClientWrapper, AsyncClientWrapper
from ...core.request_options import RequestOptions
from ...core.jsonable_encoder import jsonable_encoder
from ...types.color_or_operand import ColorOrOperand
from ...core.remove_none_from_dict import remove_none_from_dict


class QueryParamClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
    def send(self, *, operand: Operand, maybe_operand: typing.Optional[Operand] = None, operand_or_color: ColorOrOperand, maybe_operand_or_color: typing.Optional[ColorOrOperand] = None, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters:
            - operand: Operand.
            
            - maybe_operand: typing.Optional[Operand].
            
            - operand_or_color: ColorOrOperand.
            
            - maybe_operand_or_color: typing.Optional[ColorOrOperand].
            
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import SeedEnum
        from seed import Operand
        from seed import Color
        client = SeedEnum(base_url="https://yourhost.com/path/to/api", )
        client.query_param.send(operand=Operand.GREATER_THAN, operand_or_color=Color.RED, )
        """
        _response = self._client_wrapper.httpx_client.request("POST", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "query"), 
            params=jsonable_encoder(remove_none_from_dict({"operand": operand, "maybeOperand": maybe_operand, "operandOrColor": operand_or_color, "maybeOperandOrColor": maybe_operand_or_color, **(request_options.get('additional_query_parameters', {}) if request_options is not None else {}),},
            )),
            json=jsonable_encoder(remove_none_from_dict(request_options.get('additional_body_parameters', {}))) if request_options is not None else None,
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
    def send_list(self, *, operand: typing.Union[Operand, typing.Sequence[Operand]], maybe_operand: typing.Optional[typing.Union[Operand, typing.Sequence[Operand]]] = None, operand_or_color: typing.Union[ColorOrOperand, typing.Sequence[ColorOrOperand]], maybe_operand_or_color: typing.Optional[typing.Union[ColorOrOperand, typing.Sequence[ColorOrOperand]]] = None, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters:
            - operand: typing.Union[Operand, typing.Sequence[Operand]].
            
            - maybe_operand: typing.Optional[typing.Union[Operand, typing.Sequence[Operand]]].
            
            - operand_or_color: typing.Union[ColorOrOperand, typing.Sequence[ColorOrOperand]].
            
            - maybe_operand_or_color: typing.Optional[typing.Union[ColorOrOperand, typing.Sequence[ColorOrOperand]]].
            
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import SeedEnum
        from seed import Operand
        from seed import Color
        client = SeedEnum(base_url="https://yourhost.com/path/to/api", )
        client.query_param.send_list(operand=Operand.GREATER_THAN, maybe_operand=Operand.GREATER_THAN, operand_or_color=Color.RED, maybe_operand_or_color=Color.RED, )
        """
        _response = self._client_wrapper.httpx_client.request("POST", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "query-list"), 
            params=jsonable_encoder(remove_none_from_dict({"operand": operand, "maybeOperand": maybe_operand, "operandOrColor": operand_or_color, "maybeOperandOrColor": maybe_operand_or_color, **(request_options.get('additional_query_parameters', {}) if request_options is not None else {}),},
            )),
            json=jsonable_encoder(remove_none_from_dict(request_options.get('additional_body_parameters', {}))) if request_options is not None else None,
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
class AsyncQueryParamClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
    async def send(self, *, operand: Operand, maybe_operand: typing.Optional[Operand] = None, operand_or_color: ColorOrOperand, maybe_operand_or_color: typing.Optional[ColorOrOperand] = None, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters:
            - operand: Operand.
            
            - maybe_operand: typing.Optional[Operand].
            
            - operand_or_color: ColorOrOperand.
            
            - maybe_operand_or_color: typing.Optional[ColorOrOperand].
            
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import AsyncSeedEnum
        from seed import Operand
        from seed import Color
        client = AsyncSeedEnum(base_url="https://yourhost.com/path/to/api", )
        await client.query_param.send(operand=Operand.GREATER_THAN, operand_or_color=Color.RED, )
        """
        _response = await self._client_wrapper.httpx_client.request("POST", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "query"), 
            params=jsonable_encoder(remove_none_from_dict({"operand": operand, "maybeOperand": maybe_operand, "operandOrColor": operand_or_color, "maybeOperandOrColor": maybe_operand_or_color, **(request_options.get('additional_query_parameters', {}) if request_options is not None else {}),},
            )),
            json=jsonable_encoder(remove_none_from_dict(request_options.get('additional_body_parameters', {}))) if request_options is not None else None,
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
    async def send_list(self, *, operand: typing.Union[Operand, typing.Sequence[Operand]], maybe_operand: typing.Optional[typing.Union[Operand, typing.Sequence[Operand]]] = None, operand_or_color: typing.Union[ColorOrOperand, typing.Sequence[ColorOrOperand]], maybe_operand_or_color: typing.Optional[typing.Union[ColorOrOperand, typing.Sequence[ColorOrOperand]]] = None, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters:
            - operand: typing.Union[Operand, typing.Sequence[Operand]].
            
            - maybe_operand: typing.Optional[typing.Union[Operand, typing.Sequence[Operand]]].
            
            - operand_or_color: typing.Union[ColorOrOperand, typing.Sequence[ColorOrOperand]].
            
            - maybe_operand_or_color: typing.Optional[typing.Union[ColorOrOperand, typing.Sequence[ColorOrOperand]]].
            
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import AsyncSeedEnum
        from seed import Operand
        from seed import Color
        client = AsyncSeedEnum(base_url="https://yourhost.com/path/to/api", )
        await client.query_param.send_list(operand=Operand.GREATER_THAN, maybe_operand=Operand.GREATER_THAN, operand_or_color=Color.RED, maybe_operand_or_color=Color.RED, )
        """
        _response = await self._client_wrapper.httpx_client.request("POST", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "query-list"), 
            params=jsonable_encoder(remove_none_from_dict({"operand": operand, "maybeOperand": maybe_operand, "operandOrColor": operand_or_color, "maybeOperandOrColor": maybe_operand_or_color, **(request_options.get('additional_query_parameters', {}) if request_options is not None else {}),},
            )),
            json=jsonable_encoder(remove_none_from_dict(request_options.get('additional_body_parameters', {}))) if request_options is not None else None,
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
