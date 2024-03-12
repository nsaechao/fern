# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import SyncClientWrapper, AsyncClientWrapper
from ...core.request_options import RequestOptions
from ...core.jsonable_encoder import jsonable_encoder
from ..commons.types.language import Language
from ...core.remove_none_from_dict import remove_none_from_dict
from .types.execution_session_response import ExecutionSessionResponse
from .types.get_execution_session_state_response import GetExecutionSessionStateResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore
            
class SubmissionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
    def create_execution_session(self, language: Language, *, request_options: typing.Optional[RequestOptions] = None) -> ExecutionSessionResponse:
        """
        Returns sessionId and execution server URL for session. Spins up server.
        
        Parameters:
            - language: Language.
            
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import SeedTrace
        from seed import Language
        client = SeedTrace(x_random_header="YOUR_X_RANDOM_HEADER", token="YOUR_TOKEN", )
        client.submission.create_execution_session(language=Language.JAVA, )
        """
        _response = self._client_wrapper.httpx_client.request("POST", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sessions/create-session/{jsonable_encoder(language)}"), 
            params=jsonable_encoder(request_options.get('additional_query_parameters') if request_options is not None else None),
            json=jsonable_encoder(remove_none_from_dict(request_options.get('additional_body_parameters', {}))) if request_options is not None else None,
            headers=jsonable_encoder(remove_none_from_dict({**self._client_wrapper.get_headers(),**(request_options.get('additional_headers', {}) if request_options is not None else {}),},
            )),
            timeout=request_options.get('timeout_in_seconds') if request_options is not None and request_options.get('timeout_in_seconds') is not None else 60,
            retries=0,
            max_retries=request_options.get('max_retries') if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ExecutionSessionResponse, _response_json)# type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
    def get_execution_session(self, session_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Optional[ExecutionSessionResponse]:
        """
        Returns execution server URL for session. Returns empty if session isn't registered.
        
        Parameters:
            - session_id: str.
            
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import SeedTrace
        client = SeedTrace(x_random_header="YOUR_X_RANDOM_HEADER", token="YOUR_TOKEN", )
        client.submission.get_execution_session(session_id="string", )
        """
        _response = self._client_wrapper.httpx_client.request("GET", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sessions/{jsonable_encoder(session_id)}"), 
            params=jsonable_encoder(request_options.get('additional_query_parameters') if request_options is not None else None),
            headers=jsonable_encoder(remove_none_from_dict({**self._client_wrapper.get_headers(),**(request_options.get('additional_headers', {}) if request_options is not None else {}),},
            )),
            timeout=request_options.get('timeout_in_seconds') if request_options is not None and request_options.get('timeout_in_seconds') is not None else 60,
            retries=0,
            max_retries=request_options.get('max_retries') if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Optional[ExecutionSessionResponse], _response_json)# type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
    def stop_execution_session(self, session_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Stops execution session.
        
        Parameters:
            - session_id: str.
            
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import SeedTrace
        client = SeedTrace(x_random_header="YOUR_X_RANDOM_HEADER", token="YOUR_TOKEN", )
        client.submission.stop_execution_session(session_id="string", )
        """
        _response = self._client_wrapper.httpx_client.request("DELETE", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sessions/stop/{jsonable_encoder(session_id)}"), 
            params=jsonable_encoder(request_options.get('additional_query_parameters') if request_options is not None else None),
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
    def get_execution_sessions_state(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetExecutionSessionStateResponse:
        """
        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import SeedTrace
        client = SeedTrace(x_random_header="YOUR_X_RANDOM_HEADER", token="YOUR_TOKEN", )
        client.submission.get_execution_sessions_state()
        """
        _response = self._client_wrapper.httpx_client.request("GET", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "sessions/execution-sessions-state"), 
            params=jsonable_encoder(request_options.get('additional_query_parameters') if request_options is not None else None),
            headers=jsonable_encoder(remove_none_from_dict({**self._client_wrapper.get_headers(),**(request_options.get('additional_headers', {}) if request_options is not None else {}),},
            )),
            timeout=request_options.get('timeout_in_seconds') if request_options is not None and request_options.get('timeout_in_seconds') is not None else 60,
            retries=0,
            max_retries=request_options.get('max_retries') if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetExecutionSessionStateResponse, _response_json)# type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
class AsyncSubmissionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
    async def create_execution_session(self, language: Language, *, request_options: typing.Optional[RequestOptions] = None) -> ExecutionSessionResponse:
        """
        Returns sessionId and execution server URL for session. Spins up server.
        
        Parameters:
            - language: Language.
            
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import AsyncSeedTrace
        from seed import Language
        client = AsyncSeedTrace(x_random_header="YOUR_X_RANDOM_HEADER", token="YOUR_TOKEN", )
        await client.submission.create_execution_session(language=Language.JAVA, )
        """
        _response = await self._client_wrapper.httpx_client.request("POST", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sessions/create-session/{jsonable_encoder(language)}"), 
            params=jsonable_encoder(request_options.get('additional_query_parameters') if request_options is not None else None),
            json=jsonable_encoder(remove_none_from_dict(request_options.get('additional_body_parameters', {}))) if request_options is not None else None,
            headers=jsonable_encoder(remove_none_from_dict({**self._client_wrapper.get_headers(),**(request_options.get('additional_headers', {}) if request_options is not None else {}),},
            )),
            timeout=request_options.get('timeout_in_seconds') if request_options is not None and request_options.get('timeout_in_seconds') is not None else 60,
            retries=0,
            max_retries=request_options.get('max_retries') if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ExecutionSessionResponse, _response_json)# type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
    async def get_execution_session(self, session_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Optional[ExecutionSessionResponse]:
        """
        Returns execution server URL for session. Returns empty if session isn't registered.
        
        Parameters:
            - session_id: str.
            
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import AsyncSeedTrace
        client = AsyncSeedTrace(x_random_header="YOUR_X_RANDOM_HEADER", token="YOUR_TOKEN", )
        await client.submission.get_execution_session(session_id="string", )
        """
        _response = await self._client_wrapper.httpx_client.request("GET", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sessions/{jsonable_encoder(session_id)}"), 
            params=jsonable_encoder(request_options.get('additional_query_parameters') if request_options is not None else None),
            headers=jsonable_encoder(remove_none_from_dict({**self._client_wrapper.get_headers(),**(request_options.get('additional_headers', {}) if request_options is not None else {}),},
            )),
            timeout=request_options.get('timeout_in_seconds') if request_options is not None and request_options.get('timeout_in_seconds') is not None else 60,
            retries=0,
            max_retries=request_options.get('max_retries') if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Optional[ExecutionSessionResponse], _response_json)# type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
    async def stop_execution_session(self, session_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Stops execution session.
        
        Parameters:
            - session_id: str.
            
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import AsyncSeedTrace
        client = AsyncSeedTrace(x_random_header="YOUR_X_RANDOM_HEADER", token="YOUR_TOKEN", )
        await client.submission.stop_execution_session(session_id="string", )
        """
        _response = await self._client_wrapper.httpx_client.request("DELETE", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"sessions/stop/{jsonable_encoder(session_id)}"), 
            params=jsonable_encoder(request_options.get('additional_query_parameters') if request_options is not None else None),
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
    async def get_execution_sessions_state(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetExecutionSessionStateResponse:
        """
        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import AsyncSeedTrace
        client = AsyncSeedTrace(x_random_header="YOUR_X_RANDOM_HEADER", token="YOUR_TOKEN", )
        await client.submission.get_execution_sessions_state()
        """
        _response = await self._client_wrapper.httpx_client.request("GET", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "sessions/execution-sessions-state"), 
            params=jsonable_encoder(request_options.get('additional_query_parameters') if request_options is not None else None),
            headers=jsonable_encoder(remove_none_from_dict({**self._client_wrapper.get_headers(),**(request_options.get('additional_headers', {}) if request_options is not None else {}),},
            )),
            timeout=request_options.get('timeout_in_seconds') if request_options is not None and request_options.get('timeout_in_seconds') is not None else 60,
            retries=0,
            max_retries=request_options.get('max_retries') if request_options is not None else 0,  # type: ignore
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetExecutionSessionStateResponse, _response_json)# type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
