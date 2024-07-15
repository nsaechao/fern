# This file was auto-generated by Fern from our API Definition.

from ....core.abstract_fern_service import AbstractFernService
import typing
import abc
import fastapi
import inspect
from ...general_errors.errors.bad_request_body import BadRequestBody
from ....core.exceptions.fern_http_exception import FernHTTPException
import logging
import functools
from ....core.route_args import get_route_args
class AbstractNoAuthService(AbstractFernService):
    """
    AbstractNoAuthService is an abstract class containing the methods that you should implement.
    
    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """
    
    @abc.abstractmethod
    def post_with_no_auth(self, *, body: typing.Any) -> bool:
        """
        POST request with no auth
        """
        ...
    
    """
    Below are internal methods used by Fern to register your implementation.
    You can ignore them.
    """
    
    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_post_with_no_auth(router=router)
    
    @classmethod
    def __init_post_with_no_auth(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.post_with_no_auth)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls.post_with_no_auth, "__signature__", endpoint_function.replace(parameters=new_parameters))
        
        @functools.wraps(cls.post_with_no_auth)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> bool:
            try:
                return cls.post_with_no_auth(*args, **kwargs)
            except BadRequestBody as e:
                raise e
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'post_with_no_auth' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e
        
        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.post_with_no_auth.__globals__)
        
        router.post(
            path="/no-auth",
            response_model=bool,
            description=AbstractNoAuthService.post_with_no_auth.__doc__,
            **get_route_args(cls.post_with_no_auth, default_tag="no_auth"),
        )(wrapper)
