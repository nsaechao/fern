# This file was auto-generated by Fern from our API Definition.

import abc
import functools
import inspect
import logging
import typing
import uuid

import fastapi

from ....core.abstract_fern_service import AbstractFernService
from ....core.exceptions.fern_http_exception import FernHTTPException
from ....core.route_args import get_route_args
from ....types.username_cursor import UsernameCursor
from ..types.list_users_extended_response import ListUsersExtendedResponse
from ..types.list_users_pagination_response import ListUsersPaginationResponse
from ..types.order import Order
from ..types.username_container import UsernameContainer


class AbstractUsersService(AbstractFernService):
    """
    AbstractUsersService is an abstract class containing the methods that you should implement.
    
    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """
    
    @abc.abstractmethod
    def list_with_cursor_pagination(self, *, page: typing.Optional[int] = None, per_page: typing.Optional[int] = None, order: typing.Optional[Order] = None, starting_after: typing.Optional[str] = None) -> ListUsersPaginationResponse:
        ...
    
    @abc.abstractmethod
    def list_with_offset_pagination(self, *, page: typing.Optional[int] = None, per_page: typing.Optional[int] = None, order: typing.Optional[Order] = None, starting_after: typing.Optional[str] = None) -> ListUsersPaginationResponse:
        ...
    
    @abc.abstractmethod
    def list_with_offset_step_pagination(self, *, page: typing.Optional[int] = None, limit: typing.Optional[int] = None, order: typing.Optional[Order] = None) -> ListUsersPaginationResponse:
        ...
    
    @abc.abstractmethod
    def list_with_extended_results(self, *, cursor: typing.Optional[uuid.UUID] = None) -> ListUsersExtendedResponse:
        ...
    
    @abc.abstractmethod
    def list_usernames(self, *, starting_after: typing.Optional[str] = None) -> UsernameCursor:
        ...
    
    @abc.abstractmethod
    def list_with_global_config(self, *, offset: typing.Optional[int] = None) -> UsernameContainer:
        ...
    
    """
    Below are internal methods used by Fern to register your implementation.
    You can ignore them.
    """
    
    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_list_with_cursor_pagination(router=router)
        cls.__init_list_with_offset_pagination(router=router)
        cls.__init_list_with_offset_step_pagination(router=router)
        cls.__init_list_with_extended_results(router=router)
        cls.__init_list_usernames(router=router)
        cls.__init_list_with_global_config(router=router)
    
    @classmethod
    def __init_list_with_cursor_pagination(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.list_with_cursor_pagination)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "page":
                new_parameters.append(parameter.replace(default=fastapi.Query(default=None, description="Defaults to first pageDefaults to first page")))
            elif parameter_name == "per_page":
                new_parameters.append(parameter.replace(default=fastapi.Query(default=None, description="Defaults to per pageDefaults to per page")))
            elif parameter_name == "order":
                new_parameters.append(parameter.replace(default=fastapi.Query(default=None)))
            elif parameter_name == "starting_after":
                new_parameters.append(parameter.replace(default=fastapi.Query(default=None, description="The cursor used for pagination in order to fetch\nthe next page of results.The cursor used for pagination in order to fetch
                the next page of results.")))
            else:
                new_parameters.append(parameter)
        setattr(cls.list_with_cursor_pagination, "__signature__", endpoint_function.replace(parameters=new_parameters))
        
        @functools.wraps(cls.list_with_cursor_pagination)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> ListUsersPaginationResponse:
            try:
                return cls.list_with_cursor_pagination(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'list_with_cursor_pagination' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e
        
        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.list_with_cursor_pagination.__globals__)
        
        router.get(
            path="/users",
            response_model=ListUsersPaginationResponse,
            description=AbstractUsersService.list_with_cursor_pagination.__doc__,
            **get_route_args(cls.list_with_cursor_pagination, default_tag="users"),
        )(wrapper)
    
    @classmethod
    def __init_list_with_offset_pagination(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.list_with_offset_pagination)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "page":
                new_parameters.append(parameter.replace(default=fastapi.Query(default=None, description="Defaults to first pageDefaults to first page")))
            elif parameter_name == "per_page":
                new_parameters.append(parameter.replace(default=fastapi.Query(default=None, description="Defaults to per pageDefaults to per page")))
            elif parameter_name == "order":
                new_parameters.append(parameter.replace(default=fastapi.Query(default=None)))
            elif parameter_name == "starting_after":
                new_parameters.append(parameter.replace(default=fastapi.Query(default=None, description="The cursor used for pagination in order to fetch\nthe next page of results.The cursor used for pagination in order to fetch
                the next page of results.")))
            else:
                new_parameters.append(parameter)
        setattr(cls.list_with_offset_pagination, "__signature__", endpoint_function.replace(parameters=new_parameters))
        
        @functools.wraps(cls.list_with_offset_pagination)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> ListUsersPaginationResponse:
            try:
                return cls.list_with_offset_pagination(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'list_with_offset_pagination' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e
        
        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.list_with_offset_pagination.__globals__)
        
        router.get(
            path="/users",
            response_model=ListUsersPaginationResponse,
            description=AbstractUsersService.list_with_offset_pagination.__doc__,
            **get_route_args(cls.list_with_offset_pagination, default_tag="users"),
        )(wrapper)
    
    @classmethod
    def __init_list_with_offset_step_pagination(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.list_with_offset_step_pagination)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "page":
                new_parameters.append(parameter.replace(default=fastapi.Query(default=None, description="Defaults to first pageDefaults to first page")))
            elif parameter_name == "limit":
                new_parameters.append(parameter.replace(default=fastapi.Query(default=None, description="The maxiumum number of elements to return.\nThis is also used as the step size in this\npaginated endpoint.The maxiumum number of elements to return.
                This is also used as the step size in this
                paginated endpoint.")))
            elif parameter_name == "order":
                new_parameters.append(parameter.replace(default=fastapi.Query(default=None)))
            else:
                new_parameters.append(parameter)
        setattr(cls.list_with_offset_step_pagination, "__signature__", endpoint_function.replace(parameters=new_parameters))
        
        @functools.wraps(cls.list_with_offset_step_pagination)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> ListUsersPaginationResponse:
            try:
                return cls.list_with_offset_step_pagination(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'list_with_offset_step_pagination' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e
        
        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.list_with_offset_step_pagination.__globals__)
        
        router.get(
            path="/users",
            response_model=ListUsersPaginationResponse,
            description=AbstractUsersService.list_with_offset_step_pagination.__doc__,
            **get_route_args(cls.list_with_offset_step_pagination, default_tag="users"),
        )(wrapper)
    
    @classmethod
    def __init_list_with_extended_results(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.list_with_extended_results)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "cursor":
                new_parameters.append(parameter.replace(default=fastapi.Query(default=None)))
            else:
                new_parameters.append(parameter)
        setattr(cls.list_with_extended_results, "__signature__", endpoint_function.replace(parameters=new_parameters))
        
        @functools.wraps(cls.list_with_extended_results)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> ListUsersExtendedResponse:
            try:
                return cls.list_with_extended_results(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'list_with_extended_results' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e
        
        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.list_with_extended_results.__globals__)
        
        router.get(
            path="/users",
            response_model=ListUsersExtendedResponse,
            description=AbstractUsersService.list_with_extended_results.__doc__,
            **get_route_args(cls.list_with_extended_results, default_tag="users"),
        )(wrapper)
    
    @classmethod
    def __init_list_usernames(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.list_usernames)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "starting_after":
                new_parameters.append(parameter.replace(default=fastapi.Query(default=None, description="The cursor used for pagination in order to fetch\nthe next page of results.The cursor used for pagination in order to fetch
                the next page of results.")))
            else:
                new_parameters.append(parameter)
        setattr(cls.list_usernames, "__signature__", endpoint_function.replace(parameters=new_parameters))
        
        @functools.wraps(cls.list_usernames)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> UsernameCursor:
            try:
                return cls.list_usernames(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'list_usernames' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e
        
        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.list_usernames.__globals__)
        
        router.get(
            path="/users",
            response_model=UsernameCursor,
            description=AbstractUsersService.list_usernames.__doc__,
            **get_route_args(cls.list_usernames, default_tag="users"),
        )(wrapper)
    
    @classmethod
    def __init_list_with_global_config(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.list_with_global_config)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "offset":
                new_parameters.append(parameter.replace(default=fastapi.Query(default=None)))
            else:
                new_parameters.append(parameter)
        setattr(cls.list_with_global_config, "__signature__", endpoint_function.replace(parameters=new_parameters))
        
        @functools.wraps(cls.list_with_global_config)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> UsernameContainer:
            try:
                return cls.list_with_global_config(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'list_with_global_config' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e
        
        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.list_with_global_config.__globals__)
        
        router.get(
            path="/users",
            response_model=UsernameContainer,
            description=AbstractUsersService.list_with_global_config.__doc__,
            **get_route_args(cls.list_with_global_config, default_tag="users"),
        )(wrapper)
