# This file was auto-generated by Fern from our API Definition.

import typing
import uuid
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pagination import AsyncPager, SyncPager
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.username_cursor import UsernameCursor
from .types.list_users_extended_response import ListUsersExtendedResponse
from .types.list_users_pagination_response import ListUsersPaginationResponse
from .types.order import Order
from .types.user import User
from .types.username_container import UsernameContainer


class UsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_with_cursor_pagination(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        order: typing.Optional[Order] = None,
        starting_after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None
    ) -> SyncPager[User]:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            Defaults to first page

        per_page : typing.Optional[int]
            Defaults to per page

        order : typing.Optional[Order]

        starting_after : typing.Optional[str]
            The cursor used for pagination in order to fetch
            the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[User]

        Examples
        --------
        from seed.client import SeedPagination

        client = SeedPagination(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.users.list_with_cursor_pagination(
            page=1,
            per_page=1,
            order="asc",
            starting_after="string",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        _response = self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            params={"page": page, "per_page": per_page, "order": order, "starting_after": starting_after},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(ListUsersPaginationResponse, parse_obj_as(type_=ListUsersPaginationResponse, object_=_response.json()))  # type: ignore
                _has_next = False
                _get_next = None
                if _parsed_response.page is not None and _parsed_response.page.next is not None:
                    _parsed_next = _parsed_response.page.next.starting_after
                    _has_next = _parsed_next is not None
                    _get_next = lambda: self.list_with_cursor_pagination(
                        page=page,
                        per_page=per_page,
                        order=order,
                        starting_after=_parsed_next,
                        request_options=request_options,
                    )
                _items = _parsed_response.data
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_with_offset_pagination(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        order: typing.Optional[Order] = None,
        starting_after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None
    ) -> SyncPager[User]:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            Defaults to first page

        per_page : typing.Optional[int]
            Defaults to per page

        order : typing.Optional[Order]

        starting_after : typing.Optional[str]
            The cursor used for pagination in order to fetch
            the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[User]

        Examples
        --------
        from seed.client import SeedPagination

        client = SeedPagination(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.users.list_with_offset_pagination(
            page=1,
            per_page=1,
            order="asc",
            starting_after="string",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        page = page if page is not None else 1
        _response = self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            params={"page": page, "per_page": per_page, "order": order, "starting_after": starting_after},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(ListUsersPaginationResponse, parse_obj_as(type_=ListUsersPaginationResponse, object_=_response.json()))  # type: ignore
                _has_next = True
                _get_next = lambda: self.list_with_offset_pagination(
                    page=page + 1,
                    per_page=per_page,
                    order=order,
                    starting_after=starting_after,
                    request_options=request_options,
                )
                _items = _parsed_response.data
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_with_offset_step_pagination(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[Order] = None,
        request_options: typing.Optional[RequestOptions] = None
    ) -> SyncPager[User]:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            Defaults to first page

        limit : typing.Optional[int]
            The maxiumum number of elements to return.
            This is also used as the step size in this
            paginated endpoint.

        order : typing.Optional[Order]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[User]

        Examples
        --------
        from seed.client import SeedPagination

        client = SeedPagination(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.users.list_with_offset_step_pagination(
            page=1,
            limit=1,
            order="asc",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        page = page if page is not None else 1
        _response = self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            params={"page": page, "limit": limit, "order": order},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(ListUsersPaginationResponse, parse_obj_as(type_=ListUsersPaginationResponse, object_=_response.json()))  # type: ignore
                _has_next = True
                _get_next = lambda: self.list_with_offset_step_pagination(
                    page=page + 1, limit=limit, order=order, request_options=request_options
                )
                _items = _parsed_response.data
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_with_extended_results(
        self, *, cursor: typing.Optional[uuid.UUID] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> SyncPager[User]:
        """
        Parameters
        ----------
        cursor : typing.Optional[uuid.UUID]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[User]

        Examples
        --------
        import uuid

        from seed.client import SeedPagination

        client = SeedPagination(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.users.list_with_extended_results(
            cursor=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        _response = self._client_wrapper.httpx_client.request(
            "users", method="GET", params={"cursor": jsonable_encoder(cursor)}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(ListUsersExtendedResponse, parse_obj_as(type_=ListUsersExtendedResponse, object_=_response.json()))  # type: ignore
                _parsed_next = _parsed_response.next
                _has_next = _parsed_next is not None
                _get_next = lambda: self.list_with_extended_results(
                    cursor=_parsed_next, request_options=request_options
                )
                _items = []
                if _parsed_response.data is not None:
                    _items = _parsed_response.data.users
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_usernames(
        self, *, starting_after: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> SyncPager[str]:
        """
        Parameters
        ----------
        starting_after : typing.Optional[str]
            The cursor used for pagination in order to fetch
            the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[str]

        Examples
        --------
        from seed.client import SeedPagination

        client = SeedPagination(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.users.list_usernames(
            starting_after="string",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        _response = self._client_wrapper.httpx_client.request(
            "users", method="GET", params={"starting_after": starting_after}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(UsernameCursor, parse_obj_as(type_=UsernameCursor, object_=_response.json()))  # type: ignore
                _has_next = False
                _get_next = None
                if _parsed_response.cursor is not None:
                    _parsed_next = _parsed_response.cursor.after
                    _has_next = _parsed_next is not None
                    _get_next = lambda: self.list_usernames(
                        starting_after=_parsed_next, request_options=request_options
                    )
                _items = []
                if _parsed_response.cursor is not None:
                    _items = _parsed_response.cursor.data
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_with_global_config(
        self, *, offset: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> SyncPager[str]:
        """
        Parameters
        ----------
        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[str]

        Examples
        --------
        from seed.client import SeedPagination

        client = SeedPagination(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.users.list_with_global_config(
            offset=1,
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        offset = offset if offset is not None else 1
        _response = self._client_wrapper.httpx_client.request(
            "users", method="GET", params={"offset": offset}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(UsernameContainer, parse_obj_as(type_=UsernameContainer, object_=_response.json()))  # type: ignore
                _has_next = True
                _get_next = lambda: self.list_with_global_config(offset=offset + 1, request_options=request_options)
                _items = _parsed_response.results
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_with_cursor_pagination(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        order: typing.Optional[Order] = None,
        starting_after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncPager[User]:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            Defaults to first page

        per_page : typing.Optional[int]
            Defaults to per page

        order : typing.Optional[Order]

        starting_after : typing.Optional[str]
            The cursor used for pagination in order to fetch
            the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[User]

        Examples
        --------
        import asyncio

        from seed.client import AsyncSeedPagination

        client = AsyncSeedPagination(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.users.list_with_cursor_pagination(
                page=1,
                per_page=1,
                order="asc",
                starting_after="string",
            )
            async for item in response:
                yield item
            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            params={"page": page, "per_page": per_page, "order": order, "starting_after": starting_after},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(ListUsersPaginationResponse, parse_obj_as(type_=ListUsersPaginationResponse, object_=_response.json()))  # type: ignore
                _has_next = False
                _get_next = None
                if _parsed_response.page is not None and _parsed_response.page.next is not None:
                    _parsed_next = _parsed_response.page.next.starting_after
                    _has_next = _parsed_next is not None
                    _get_next = lambda: self.list_with_cursor_pagination(
                        page=page,
                        per_page=per_page,
                        order=order,
                        starting_after=_parsed_next,
                        request_options=request_options,
                    )
                _items = _parsed_response.data
                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_with_offset_pagination(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        order: typing.Optional[Order] = None,
        starting_after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncPager[User]:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            Defaults to first page

        per_page : typing.Optional[int]
            Defaults to per page

        order : typing.Optional[Order]

        starting_after : typing.Optional[str]
            The cursor used for pagination in order to fetch
            the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[User]

        Examples
        --------
        import asyncio

        from seed.client import AsyncSeedPagination

        client = AsyncSeedPagination(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.users.list_with_offset_pagination(
                page=1,
                per_page=1,
                order="asc",
                starting_after="string",
            )
            async for item in response:
                yield item
            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        page = page if page is not None else 1
        _response = await self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            params={"page": page, "per_page": per_page, "order": order, "starting_after": starting_after},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(ListUsersPaginationResponse, parse_obj_as(type_=ListUsersPaginationResponse, object_=_response.json()))  # type: ignore
                _has_next = True
                _get_next = lambda: self.list_with_offset_pagination(
                    page=page + 1,
                    per_page=per_page,
                    order=order,
                    starting_after=starting_after,
                    request_options=request_options,
                )
                _items = _parsed_response.data
                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_with_offset_step_pagination(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[Order] = None,
        request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncPager[User]:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            Defaults to first page

        limit : typing.Optional[int]
            The maxiumum number of elements to return.
            This is also used as the step size in this
            paginated endpoint.

        order : typing.Optional[Order]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[User]

        Examples
        --------
        import asyncio

        from seed.client import AsyncSeedPagination

        client = AsyncSeedPagination(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.users.list_with_offset_step_pagination(
                page=1,
                limit=1,
                order="asc",
            )
            async for item in response:
                yield item
            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        page = page if page is not None else 1
        _response = await self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            params={"page": page, "limit": limit, "order": order},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(ListUsersPaginationResponse, parse_obj_as(type_=ListUsersPaginationResponse, object_=_response.json()))  # type: ignore
                _has_next = True
                _get_next = lambda: self.list_with_offset_step_pagination(
                    page=page + 1, limit=limit, order=order, request_options=request_options
                )
                _items = _parsed_response.data
                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_with_extended_results(
        self, *, cursor: typing.Optional[uuid.UUID] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncPager[User]:
        """
        Parameters
        ----------
        cursor : typing.Optional[uuid.UUID]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[User]

        Examples
        --------
        import asyncio
        import uuid

        from seed.client import AsyncSeedPagination

        client = AsyncSeedPagination(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.users.list_with_extended_results(
                cursor=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            )
            async for item in response:
                yield item
            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users", method="GET", params={"cursor": jsonable_encoder(cursor)}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(ListUsersExtendedResponse, parse_obj_as(type_=ListUsersExtendedResponse, object_=_response.json()))  # type: ignore
                _parsed_next = _parsed_response.next
                _has_next = _parsed_next is not None
                _get_next = lambda: self.list_with_extended_results(
                    cursor=_parsed_next, request_options=request_options
                )
                _items = []
                if _parsed_response.data is not None:
                    _items = _parsed_response.data.users
                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_usernames(
        self, *, starting_after: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncPager[str]:
        """
        Parameters
        ----------
        starting_after : typing.Optional[str]
            The cursor used for pagination in order to fetch
            the next page of results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[str]

        Examples
        --------
        import asyncio

        from seed.client import AsyncSeedPagination

        client = AsyncSeedPagination(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.users.list_usernames(
                starting_after="string",
            )
            async for item in response:
                yield item
            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users", method="GET", params={"starting_after": starting_after}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(UsernameCursor, parse_obj_as(type_=UsernameCursor, object_=_response.json()))  # type: ignore
                _has_next = False
                _get_next = None
                if _parsed_response.cursor is not None:
                    _parsed_next = _parsed_response.cursor.after
                    _has_next = _parsed_next is not None
                    _get_next = lambda: self.list_usernames(
                        starting_after=_parsed_next, request_options=request_options
                    )
                _items = []
                if _parsed_response.cursor is not None:
                    _items = _parsed_response.cursor.data
                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_with_global_config(
        self, *, offset: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncPager[str]:
        """
        Parameters
        ----------
        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[str]

        Examples
        --------
        import asyncio

        from seed.client import AsyncSeedPagination

        client = AsyncSeedPagination(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.users.list_with_global_config(
                offset=1,
            )
            async for item in response:
                yield item
            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        offset = offset if offset is not None else 1
        _response = await self._client_wrapper.httpx_client.request(
            "users", method="GET", params={"offset": offset}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(UsernameContainer, parse_obj_as(type_=UsernameContainer, object_=_response.json()))  # type: ignore
                _has_next = True
                _get_next = lambda: self.list_with_global_config(offset=offset + 1, request_options=request_options)
                _items = _parsed_response.results
                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
