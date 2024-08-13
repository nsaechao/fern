# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from .running_submission_state import RunningSubmissionState
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from .workspace_run_details import WorkspaceRunDetails
from .workspace_traced_update import WorkspaceTracedUpdate
from .error_info import ErrorInfo
from ....core.pydantic_utilities import UniversalRootModel
import typing
import typing_extensions
import pydantic
from ....core.pydantic_utilities import UniversalBaseModel
from ....core.pydantic_utilities import update_forward_refs

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def running(self, value: RunningSubmissionState) -> WorkspaceSubmissionUpdateInfo:
        if IS_PYDANTIC_V2:
            return WorkspaceSubmissionUpdateInfo(
                root=_WorkspaceSubmissionUpdateInfo.Running(type="running", value=value)
            )  # type: ignore
        else:
            return WorkspaceSubmissionUpdateInfo(
                __root__=_WorkspaceSubmissionUpdateInfo.Running(
                    type="running", value=value
                )
            )  # type: ignore

    def ran(self, value: WorkspaceRunDetails) -> WorkspaceSubmissionUpdateInfo:
        if IS_PYDANTIC_V2:
            return WorkspaceSubmissionUpdateInfo(
                root=_WorkspaceSubmissionUpdateInfo.Ran(
                    **value.dict(exclude_unset=True), type="ran"
                )
            )  # type: ignore
        else:
            return WorkspaceSubmissionUpdateInfo(
                __root__=_WorkspaceSubmissionUpdateInfo.Ran(
                    **value.dict(exclude_unset=True), type="ran"
                )
            )  # type: ignore

    def stopped(self) -> WorkspaceSubmissionUpdateInfo:
        if IS_PYDANTIC_V2:
            return WorkspaceSubmissionUpdateInfo(
                root=_WorkspaceSubmissionUpdateInfo.Stopped(type="stopped")
            )  # type: ignore
        else:
            return WorkspaceSubmissionUpdateInfo(
                __root__=_WorkspaceSubmissionUpdateInfo.Stopped(type="stopped")
            )  # type: ignore

    def traced(self) -> WorkspaceSubmissionUpdateInfo:
        if IS_PYDANTIC_V2:
            return WorkspaceSubmissionUpdateInfo(
                root=_WorkspaceSubmissionUpdateInfo.Traced(type="traced")
            )  # type: ignore
        else:
            return WorkspaceSubmissionUpdateInfo(
                __root__=_WorkspaceSubmissionUpdateInfo.Traced(type="traced")
            )  # type: ignore

    def traced_v_2(self, value: WorkspaceTracedUpdate) -> WorkspaceSubmissionUpdateInfo:
        if IS_PYDANTIC_V2:
            return WorkspaceSubmissionUpdateInfo(
                root=_WorkspaceSubmissionUpdateInfo.TracedV2(
                    **value.dict(exclude_unset=True), type="tracedV2"
                )
            )  # type: ignore
        else:
            return WorkspaceSubmissionUpdateInfo(
                __root__=_WorkspaceSubmissionUpdateInfo.TracedV2(
                    **value.dict(exclude_unset=True), type="tracedV2"
                )
            )  # type: ignore

    def errored(self, value: ErrorInfo) -> WorkspaceSubmissionUpdateInfo:
        if IS_PYDANTIC_V2:
            return WorkspaceSubmissionUpdateInfo(
                root=_WorkspaceSubmissionUpdateInfo.Errored(type="errored", value=value)
            )  # type: ignore
        else:
            return WorkspaceSubmissionUpdateInfo(
                __root__=_WorkspaceSubmissionUpdateInfo.Errored(
                    type="errored", value=value
                )
            )  # type: ignore

    def finished(self) -> WorkspaceSubmissionUpdateInfo:
        if IS_PYDANTIC_V2:
            return WorkspaceSubmissionUpdateInfo(
                root=_WorkspaceSubmissionUpdateInfo.Finished(type="finished")
            )  # type: ignore
        else:
            return WorkspaceSubmissionUpdateInfo(
                __root__=_WorkspaceSubmissionUpdateInfo.Finished(type="finished")
            )  # type: ignore


class WorkspaceSubmissionUpdateInfo(UniversalRootModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    if IS_PYDANTIC_V2:
        root: typing_extensions.Annotated[
            typing.Union[
                _WorkspaceSubmissionUpdateInfo.Running,
                _WorkspaceSubmissionUpdateInfo.Ran,
                _WorkspaceSubmissionUpdateInfo.Stopped,
                _WorkspaceSubmissionUpdateInfo.Traced,
                _WorkspaceSubmissionUpdateInfo.TracedV2,
                _WorkspaceSubmissionUpdateInfo.Errored,
                _WorkspaceSubmissionUpdateInfo.Finished,
            ],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(
            self,
        ) -> typing.Union[
            _WorkspaceSubmissionUpdateInfo.Running,
            _WorkspaceSubmissionUpdateInfo.Ran,
            _WorkspaceSubmissionUpdateInfo.Stopped,
            _WorkspaceSubmissionUpdateInfo.Traced,
            _WorkspaceSubmissionUpdateInfo.TracedV2,
            _WorkspaceSubmissionUpdateInfo.Errored,
            _WorkspaceSubmissionUpdateInfo.Finished,
        ]:
            return self.root
    else:
        __root__: typing_extensions.Annotated[
            typing.Union[
                _WorkspaceSubmissionUpdateInfo.Running,
                _WorkspaceSubmissionUpdateInfo.Ran,
                _WorkspaceSubmissionUpdateInfo.Stopped,
                _WorkspaceSubmissionUpdateInfo.Traced,
                _WorkspaceSubmissionUpdateInfo.TracedV2,
                _WorkspaceSubmissionUpdateInfo.Errored,
                _WorkspaceSubmissionUpdateInfo.Finished,
            ],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(
            self,
        ) -> typing.Union[
            _WorkspaceSubmissionUpdateInfo.Running,
            _WorkspaceSubmissionUpdateInfo.Ran,
            _WorkspaceSubmissionUpdateInfo.Stopped,
            _WorkspaceSubmissionUpdateInfo.Traced,
            _WorkspaceSubmissionUpdateInfo.TracedV2,
            _WorkspaceSubmissionUpdateInfo.Errored,
            _WorkspaceSubmissionUpdateInfo.Finished,
        ]:
            return self.__root__

    def visit(
        self,
        running: typing.Callable[[RunningSubmissionState], T_Result],
        ran: typing.Callable[[WorkspaceRunDetails], T_Result],
        stopped: typing.Callable[[], T_Result],
        traced: typing.Callable[[], T_Result],
        traced_v_2: typing.Callable[[WorkspaceTracedUpdate], T_Result],
        errored: typing.Callable[[ErrorInfo], T_Result],
        finished: typing.Callable[[], T_Result],
    ) -> T_Result:
        unioned_value = self.get_as_union()
        if unioned_value.type == "running":
            return running(unioned_value.value)
        if unioned_value.type == "ran":
            return ran(
                WorkspaceRunDetails(
                    **unioned_value.dict(exclude_unset=True, exclude={"type"})
                )
            )
        if unioned_value.type == "stopped":
            return stopped()
        if unioned_value.type == "traced":
            return traced()
        if unioned_value.type == "tracedV2":
            return traced_v_2(
                WorkspaceTracedUpdate(
                    **unioned_value.dict(exclude_unset=True, exclude={"type"})
                )
            )
        if unioned_value.type == "errored":
            return errored(unioned_value.value)
        if unioned_value.type == "finished":
            return finished()


class _WorkspaceSubmissionUpdateInfo:
    class Running(UniversalBaseModel):
        type: typing.Literal["running"] = "running"
        value: RunningSubmissionState

    class Ran(WorkspaceRunDetails):
        type: typing.Literal["ran"] = "ran"

    class Stopped(UniversalBaseModel):
        type: typing.Literal["stopped"] = "stopped"

    class Traced(UniversalBaseModel):
        type: typing.Literal["traced"] = "traced"

    class TracedV2(WorkspaceTracedUpdate):
        type: typing.Literal["tracedV2"] = "tracedV2"

    class Errored(UniversalBaseModel):
        type: typing.Literal["errored"] = "errored"
        value: ErrorInfo

    class Finished(UniversalBaseModel):
        type: typing.Literal["finished"] = "finished"


update_forward_refs(WorkspaceSubmissionUpdateInfo)
