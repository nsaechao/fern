# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from typing_extensions import Self

# Generic to represent the underlying type of the results within a page
T = typing.TypeVar("T")

# SDKs implement a Page ABC per-pagination request, the endpoint then retuns a pager that wraps this type
# for example, an endpoint will return SyncPager[UserPage] where UserPage implements the Page ABC. ex:
#
# SyncPager<InnerListType>(
#     has_next=response.list_metadata.after is not None,
#     items=response.data,
#     # This should be the outer function that returns the SyncPager again
#     get_next=lambda: list(..., cursor: response.cursor) (or list(..., offset: offset + 1))
# )
class BasePage(pydantic.BaseModel, typing.Generic[T]):
    has_next: bool
    items: typing.Optional[typing.List[T]]


class SyncPage(BasePage[T], typing.Generic[T]):
    get_next: typing.Optional[typing.Callable[[], typing.Optional[Self]]]


class AsyncPage(BasePage[T], typing.Generic[T]):
    get_next: typing.Optional[typing.Callable[[], typing.Awaitable[typing.Optional[Self]]]]


# ----------------------------


class SyncPager(SyncPage[T], typing.Generic[T]):
    # Here we type ignore the iterator to avoid a mypy error
    # caused by the type conflict with Pydanitc's __iter__ method
    # brought in by extending the base model
    def __iter__(self) -> typing.Iterator[T]:  # type: ignore
        for page in self.iter_pages():
            if page.items is not None:
                for item in page.items:
                    yield item

    def iter_pages(self) -> typing.Iterator[SyncPage[T]]:
        page: typing.Union[SyncPager[T], None] = self
        while True:
            if page is not None:
                yield page
                if page.has_next and page.get_next is not None:
                    page = page.get_next()
                    if page is None or page.items is None or len(page.items) == 0:
                        return
                else:
                    return
            else:
                return

    def next_page(self) -> typing.Optional[SyncPage[T]]:
        return self.get_next() if self.get_next is not None else None


class AsyncPager(AsyncPage[T], typing.Generic[T]):
    async def __aiter__(self) -> typing.AsyncIterator[T]:  # type: ignore
        async for page in self.iter_pages():
            if page.items is not None:
                for item in page.items:
                    yield item

    async def iter_pages(self) -> typing.AsyncIterator[AsyncPage[T]]:
        page: typing.Union[AsyncPager[T], None] = self
        while True:
            if page is not None:
                yield page
                if page is not None and page.has_next and page.get_next is not None:
                    page = await page.get_next()
                    if page is None or page.items is None or len(page.items) == 0:
                        return
                else:
                    return
            else:
                return

    async def next_page(self) -> typing.Optional[AsyncPage[T]]:
        return await self.get_next() if self.get_next is not None else None
