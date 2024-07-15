# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalRootModel
from .test_submission_state import TestSubmissionState
from .workspace_submission_state import WorkspaceSubmissionState

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def test(self, value: TestSubmissionState) -> SubmissionTypeState:
        return SubmissionTypeState(_SubmissionTypeState.Test(**value.dict(exclude_unset=True), type="test"))

    def workspace(self, value: WorkspaceSubmissionState) -> SubmissionTypeState:
        return SubmissionTypeState(_SubmissionTypeState.Workspace(**value.dict(exclude_unset=True), type="workspace"))


class SubmissionTypeState(UniversalRootModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    if IS_PYDANTIC_V2:
        root: typing_extensions.Annotated[
            typing.Union[_SubmissionTypeState.Test, _SubmissionTypeState.Workspace],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(self) -> typing.Union[_SubmissionTypeState.Test, _SubmissionTypeState.Workspace]:
            return self.root

    else:
        __root__: typing_extensions.Annotated[
            typing.Union[_SubmissionTypeState.Test, _SubmissionTypeState.Workspace],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(self) -> typing.Union[_SubmissionTypeState.Test, _SubmissionTypeState.Workspace]:
            return self.__root__

    def visit(
        self,
        test: typing.Callable[[TestSubmissionState], T_Result],
        workspace: typing.Callable[[WorkspaceSubmissionState], T_Result],
    ) -> T_Result:
        if self.get_as_union().type == "test":
            return test(TestSubmissionState(**self.get_as_union().dict(exclude_unset=True, exclude={"type"})))
        if self.get_as_union().type == "workspace":
            return workspace(WorkspaceSubmissionState(**self.get_as_union().dict(exclude_unset=True, exclude={"type"})))


class _SubmissionTypeState:
    class Test(TestSubmissionState):
        type: typing.Literal["test"] = "test"

        class Config:
            allow_population_by_field_name = True

    class Workspace(WorkspaceSubmissionState):
        type: typing.Literal["workspace"] = "workspace"

        class Config:
            allow_population_by_field_name = True
