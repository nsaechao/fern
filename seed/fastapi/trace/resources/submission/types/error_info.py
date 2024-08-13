# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from .compile_error import (
    CompileError as resources_submission_types_compile_error_CompileError,
)
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from .runtime_error import (
    RuntimeError as resources_submission_types_runtime_error_RuntimeError,
)
from .internal_error import (
    InternalError as resources_submission_types_internal_error_InternalError,
)
from ....core.pydantic_utilities import UniversalRootModel
import typing
import typing_extensions
import pydantic
from ....core.pydantic_utilities import update_forward_refs

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def compile_error(
        self, value: resources_submission_types_compile_error_CompileError
    ) -> ErrorInfo:
        if IS_PYDANTIC_V2:
            return ErrorInfo(
                root=_ErrorInfo.CompileError(
                    **value.dict(exclude_unset=True), type="compileError"
                )
            )  # type: ignore
        else:
            return ErrorInfo(
                __root__=_ErrorInfo.CompileError(
                    **value.dict(exclude_unset=True), type="compileError"
                )
            )  # type: ignore

    def runtime_error(
        self, value: resources_submission_types_runtime_error_RuntimeError
    ) -> ErrorInfo:
        if IS_PYDANTIC_V2:
            return ErrorInfo(
                root=_ErrorInfo.RuntimeError(
                    **value.dict(exclude_unset=True), type="runtimeError"
                )
            )  # type: ignore
        else:
            return ErrorInfo(
                __root__=_ErrorInfo.RuntimeError(
                    **value.dict(exclude_unset=True), type="runtimeError"
                )
            )  # type: ignore

    def internal_error(
        self, value: resources_submission_types_internal_error_InternalError
    ) -> ErrorInfo:
        if IS_PYDANTIC_V2:
            return ErrorInfo(
                root=_ErrorInfo.InternalError(
                    **value.dict(exclude_unset=True), type="internalError"
                )
            )  # type: ignore
        else:
            return ErrorInfo(
                __root__=_ErrorInfo.InternalError(
                    **value.dict(exclude_unset=True), type="internalError"
                )
            )  # type: ignore


class ErrorInfo(UniversalRootModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    if IS_PYDANTIC_V2:
        root: typing_extensions.Annotated[
            typing.Union[
                _ErrorInfo.CompileError,
                _ErrorInfo.RuntimeError,
                _ErrorInfo.InternalError,
            ],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(
            self,
        ) -> typing.Union[
            _ErrorInfo.CompileError, _ErrorInfo.RuntimeError, _ErrorInfo.InternalError
        ]:
            return self.root
    else:
        __root__: typing_extensions.Annotated[
            typing.Union[
                _ErrorInfo.CompileError,
                _ErrorInfo.RuntimeError,
                _ErrorInfo.InternalError,
            ],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(
            self,
        ) -> typing.Union[
            _ErrorInfo.CompileError, _ErrorInfo.RuntimeError, _ErrorInfo.InternalError
        ]:
            return self.__root__

    def visit(
        self,
        compile_error: typing.Callable[
            [resources_submission_types_compile_error_CompileError], T_Result
        ],
        runtime_error: typing.Callable[
            [resources_submission_types_runtime_error_RuntimeError], T_Result
        ],
        internal_error: typing.Callable[
            [resources_submission_types_internal_error_InternalError], T_Result
        ],
    ) -> T_Result:
        unioned_value = self.get_as_union()
        if unioned_value.type == "compileError":
            return compile_error(
                resources_submission_types_compile_error_CompileError(
                    **unioned_value.dict(exclude_unset=True, exclude={"type"})
                )
            )
        if unioned_value.type == "runtimeError":
            return runtime_error(
                resources_submission_types_runtime_error_RuntimeError(
                    **unioned_value.dict(exclude_unset=True, exclude={"type"})
                )
            )
        if unioned_value.type == "internalError":
            return internal_error(
                resources_submission_types_internal_error_InternalError(
                    **unioned_value.dict(exclude_unset=True, exclude={"type"})
                )
            )


class _ErrorInfo:
    class CompileError(resources_submission_types_compile_error_CompileError):
        type: typing.Literal["compileError"] = "compileError"

    class RuntimeError(resources_submission_types_runtime_error_RuntimeError):
        type: typing.Literal["runtimeError"] = "runtimeError"

    class InternalError(resources_submission_types_internal_error_InternalError):
        type: typing.Literal["internalError"] = "internalError"


update_forward_refs(ErrorInfo)
