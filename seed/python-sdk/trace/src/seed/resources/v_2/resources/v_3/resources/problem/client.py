# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .......core.api_error import ApiError
from .types.problem_info_v_2 import ProblemInfoV2
from .......core.client_wrapper import SyncClientWrapper, AsyncClientWrapper
from .......core.request_options import RequestOptions
from .......core.jsonable_encoder import jsonable_encoder
from ......commons.types.problem_id import ProblemId
from .......core.remove_none_from_dict import remove_none_from_dict
from .types.lightweight_problem_info_v_2 import LightweightProblemInfoV2

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore
            
class ProblemClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
    def get_lightweight_problems(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[LightweightProblemInfoV2]:
        """
        Returns lightweight versions of all problems
        
        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import SeedTrace
        client = SeedTrace(x_random_header="YOUR_X_RANDOM_HEADER", token="YOUR_TOKEN", )
        client.v_2.v_3.problem.get_lightweight_problems()
        """
        _response = self._client_wrapper.httpx_client.request("GET", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "problems-v2/lightweight-problem-info"), 
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
            return pydantic.parse_obj_as(typing.List[LightweightProblemInfoV2], _response_json)# type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
    def get_problems(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[ProblemInfoV2]:
        """
        Returns latest versions of all problems
        
        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import SeedTrace
        client = SeedTrace(x_random_header="YOUR_X_RANDOM_HEADER", token="YOUR_TOKEN", )
        client.v_2.v_3.problem.get_problems()
        """
        _response = self._client_wrapper.httpx_client.request("GET", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "problems-v2/problem-info"), 
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
            return pydantic.parse_obj_as(typing.List[ProblemInfoV2], _response_json)# type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
    def get_latest_problem(self, problem_id: ProblemId, *, request_options: typing.Optional[RequestOptions] = None) -> ProblemInfoV2:
        """
        Returns latest version of a problem
        
        Parameters:
            - problem_id: ProblemId.
            
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import SeedTrace
        client = SeedTrace(x_random_header="YOUR_X_RANDOM_HEADER", token="YOUR_TOKEN", )
        client.v_2.v_3.problem.get_latest_problem(problem_id="string", )
        """
        _response = self._client_wrapper.httpx_client.request("GET", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"problems-v2/problem-info/{jsonable_encoder(problem_id)}"), 
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
            return pydantic.parse_obj_as(ProblemInfoV2, _response_json)# type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
    def get_problem_version(self, problem_id: ProblemId, problem_version: int, *, request_options: typing.Optional[RequestOptions] = None) -> ProblemInfoV2:
        """
        Returns requested version of a problem
        
        Parameters:
            - problem_id: ProblemId.
            
            - problem_version: int.
            
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import SeedTrace
        client = SeedTrace(x_random_header="YOUR_X_RANDOM_HEADER", token="YOUR_TOKEN", )
        client.v_2.v_3.problem.get_problem_version(problem_id="string", problem_version=1, )
        """
        _response = self._client_wrapper.httpx_client.request("GET", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"problems-v2/problem-info/{jsonable_encoder(problem_id)}/version/{jsonable_encoder(problem_version)}"), 
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
            return pydantic.parse_obj_as(ProblemInfoV2, _response_json)# type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
class AsyncProblemClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
    async def get_lightweight_problems(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[LightweightProblemInfoV2]:
        """
        Returns lightweight versions of all problems
        
        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import AsyncSeedTrace
        client = AsyncSeedTrace(x_random_header="YOUR_X_RANDOM_HEADER", token="YOUR_TOKEN", )
        await client.v_2.v_3.problem.get_lightweight_problems()
        """
        _response = await self._client_wrapper.httpx_client.request("GET", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "problems-v2/lightweight-problem-info"), 
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
            return pydantic.parse_obj_as(typing.List[LightweightProblemInfoV2], _response_json)# type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
    async def get_problems(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[ProblemInfoV2]:
        """
        Returns latest versions of all problems
        
        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import AsyncSeedTrace
        client = AsyncSeedTrace(x_random_header="YOUR_X_RANDOM_HEADER", token="YOUR_TOKEN", )
        await client.v_2.v_3.problem.get_problems()
        """
        _response = await self._client_wrapper.httpx_client.request("GET", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "problems-v2/problem-info"), 
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
            return pydantic.parse_obj_as(typing.List[ProblemInfoV2], _response_json)# type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
    async def get_latest_problem(self, problem_id: ProblemId, *, request_options: typing.Optional[RequestOptions] = None) -> ProblemInfoV2:
        """
        Returns latest version of a problem
        
        Parameters:
            - problem_id: ProblemId.
            
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import AsyncSeedTrace
        client = AsyncSeedTrace(x_random_header="YOUR_X_RANDOM_HEADER", token="YOUR_TOKEN", )
        await client.v_2.v_3.problem.get_latest_problem(problem_id="string", )
        """
        _response = await self._client_wrapper.httpx_client.request("GET", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"problems-v2/problem-info/{jsonable_encoder(problem_id)}"), 
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
            return pydantic.parse_obj_as(ProblemInfoV2, _response_json)# type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
    async def get_problem_version(self, problem_id: ProblemId, problem_version: int, *, request_options: typing.Optional[RequestOptions] = None) -> ProblemInfoV2:
        """
        Returns requested version of a problem
        
        Parameters:
            - problem_id: ProblemId.
            
            - problem_version: int.
            
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from seed.client import AsyncSeedTrace
        client = AsyncSeedTrace(x_random_header="YOUR_X_RANDOM_HEADER", token="YOUR_TOKEN", )
        await client.v_2.v_3.problem.get_problem_version(problem_id="string", problem_version=1, )
        """
        _response = await self._client_wrapper.httpx_client.request("GET", urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"problems-v2/problem-info/{jsonable_encoder(problem_id)}/version/{jsonable_encoder(problem_version)}"), 
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
            return pydantic.parse_obj_as(ProblemInfoV2, _response_json)# type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
