# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalRootModel
from .building_executor_response import BuildingExecutorResponse
from .errored_response import ErroredResponse
from .finished_response import FinishedResponse
from .graded_response import GradedResponse
from .graded_response_v_2 import GradedResponseV2
from .invalid_request_response import InvalidRequestResponse
from .recorded_response_notification import RecordedResponseNotification
from .recording_response_notification import RecordingResponseNotification
from .running_response import RunningResponse
from .stopped_response import StoppedResponse
from .workspace_ran_response import WorkspaceRanResponse

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def building_executor(self, value: BuildingExecutorResponse) -> CodeExecutionUpdate:
        if IS_PYDANTIC_V2:
            return CodeExecutionUpdate(
                root=_CodeExecutionUpdate.BuildingExecutor(**value.dict(exclude_unset=True), type="buildingExecutor")
            )
        else:
            return CodeExecutionUpdate(
                __root__=_CodeExecutionUpdate.BuildingExecutor(
                    **value.dict(exclude_unset=True), type="buildingExecutor"
                )
            )

    def running(self, value: RunningResponse) -> CodeExecutionUpdate:
        if IS_PYDANTIC_V2:
            return CodeExecutionUpdate(
                root=_CodeExecutionUpdate.Running(**value.dict(exclude_unset=True), type="running")
            )
        else:
            return CodeExecutionUpdate(
                __root__=_CodeExecutionUpdate.Running(**value.dict(exclude_unset=True), type="running")
            )

    def errored(self, value: ErroredResponse) -> CodeExecutionUpdate:
        if IS_PYDANTIC_V2:
            return CodeExecutionUpdate(
                root=_CodeExecutionUpdate.Errored(**value.dict(exclude_unset=True), type="errored")
            )
        else:
            return CodeExecutionUpdate(
                __root__=_CodeExecutionUpdate.Errored(**value.dict(exclude_unset=True), type="errored")
            )

    def stopped(self, value: StoppedResponse) -> CodeExecutionUpdate:
        if IS_PYDANTIC_V2:
            return CodeExecutionUpdate(
                root=_CodeExecutionUpdate.Stopped(**value.dict(exclude_unset=True), type="stopped")
            )
        else:
            return CodeExecutionUpdate(
                __root__=_CodeExecutionUpdate.Stopped(**value.dict(exclude_unset=True), type="stopped")
            )

    def graded(self, value: GradedResponse) -> CodeExecutionUpdate:
        if IS_PYDANTIC_V2:
            return CodeExecutionUpdate(
                root=_CodeExecutionUpdate.Graded(**value.dict(exclude_unset=True), type="graded")
            )
        else:
            return CodeExecutionUpdate(
                __root__=_CodeExecutionUpdate.Graded(**value.dict(exclude_unset=True), type="graded")
            )

    def graded_v_2(self, value: GradedResponseV2) -> CodeExecutionUpdate:
        if IS_PYDANTIC_V2:
            return CodeExecutionUpdate(
                root=_CodeExecutionUpdate.GradedV2(**value.dict(exclude_unset=True), type="gradedV2")
            )
        else:
            return CodeExecutionUpdate(
                __root__=_CodeExecutionUpdate.GradedV2(**value.dict(exclude_unset=True), type="gradedV2")
            )

    def workspace_ran(self, value: WorkspaceRanResponse) -> CodeExecutionUpdate:
        if IS_PYDANTIC_V2:
            return CodeExecutionUpdate(
                root=_CodeExecutionUpdate.WorkspaceRan(**value.dict(exclude_unset=True), type="workspaceRan")
            )
        else:
            return CodeExecutionUpdate(
                __root__=_CodeExecutionUpdate.WorkspaceRan(**value.dict(exclude_unset=True), type="workspaceRan")
            )

    def recording(self, value: RecordingResponseNotification) -> CodeExecutionUpdate:
        if IS_PYDANTIC_V2:
            return CodeExecutionUpdate(
                root=_CodeExecutionUpdate.Recording(**value.dict(exclude_unset=True), type="recording")
            )
        else:
            return CodeExecutionUpdate(
                __root__=_CodeExecutionUpdate.Recording(**value.dict(exclude_unset=True), type="recording")
            )

    def recorded(self, value: RecordedResponseNotification) -> CodeExecutionUpdate:
        if IS_PYDANTIC_V2:
            return CodeExecutionUpdate(
                root=_CodeExecutionUpdate.Recorded(**value.dict(exclude_unset=True), type="recorded")
            )
        else:
            return CodeExecutionUpdate(
                __root__=_CodeExecutionUpdate.Recorded(**value.dict(exclude_unset=True), type="recorded")
            )

    def invalid_request(self, value: InvalidRequestResponse) -> CodeExecutionUpdate:
        if IS_PYDANTIC_V2:
            return CodeExecutionUpdate(
                root=_CodeExecutionUpdate.InvalidRequest(**value.dict(exclude_unset=True), type="invalidRequest")
            )
        else:
            return CodeExecutionUpdate(
                __root__=_CodeExecutionUpdate.InvalidRequest(**value.dict(exclude_unset=True), type="invalidRequest")
            )

    def finished(self, value: FinishedResponse) -> CodeExecutionUpdate:
        if IS_PYDANTIC_V2:
            return CodeExecutionUpdate(
                root=_CodeExecutionUpdate.Finished(**value.dict(exclude_unset=True), type="finished")
            )
        else:
            return CodeExecutionUpdate(
                __root__=_CodeExecutionUpdate.Finished(**value.dict(exclude_unset=True), type="finished")
            )


class CodeExecutionUpdate(UniversalRootModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    if IS_PYDANTIC_V2:
        root: typing_extensions.Annotated[
            typing.Union[
                _CodeExecutionUpdate.BuildingExecutor,
                _CodeExecutionUpdate.Running,
                _CodeExecutionUpdate.Errored,
                _CodeExecutionUpdate.Stopped,
                _CodeExecutionUpdate.Graded,
                _CodeExecutionUpdate.GradedV2,
                _CodeExecutionUpdate.WorkspaceRan,
                _CodeExecutionUpdate.Recording,
                _CodeExecutionUpdate.Recorded,
                _CodeExecutionUpdate.InvalidRequest,
                _CodeExecutionUpdate.Finished,
            ],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(
            self,
        ) -> typing.Union[
            _CodeExecutionUpdate.BuildingExecutor,
            _CodeExecutionUpdate.Running,
            _CodeExecutionUpdate.Errored,
            _CodeExecutionUpdate.Stopped,
            _CodeExecutionUpdate.Graded,
            _CodeExecutionUpdate.GradedV2,
            _CodeExecutionUpdate.WorkspaceRan,
            _CodeExecutionUpdate.Recording,
            _CodeExecutionUpdate.Recorded,
            _CodeExecutionUpdate.InvalidRequest,
            _CodeExecutionUpdate.Finished,
        ]:
            return self.root

    else:
        __root__: typing_extensions.Annotated[
            typing.Union[
                _CodeExecutionUpdate.BuildingExecutor,
                _CodeExecutionUpdate.Running,
                _CodeExecutionUpdate.Errored,
                _CodeExecutionUpdate.Stopped,
                _CodeExecutionUpdate.Graded,
                _CodeExecutionUpdate.GradedV2,
                _CodeExecutionUpdate.WorkspaceRan,
                _CodeExecutionUpdate.Recording,
                _CodeExecutionUpdate.Recorded,
                _CodeExecutionUpdate.InvalidRequest,
                _CodeExecutionUpdate.Finished,
            ],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(
            self,
        ) -> typing.Union[
            _CodeExecutionUpdate.BuildingExecutor,
            _CodeExecutionUpdate.Running,
            _CodeExecutionUpdate.Errored,
            _CodeExecutionUpdate.Stopped,
            _CodeExecutionUpdate.Graded,
            _CodeExecutionUpdate.GradedV2,
            _CodeExecutionUpdate.WorkspaceRan,
            _CodeExecutionUpdate.Recording,
            _CodeExecutionUpdate.Recorded,
            _CodeExecutionUpdate.InvalidRequest,
            _CodeExecutionUpdate.Finished,
        ]:
            return self.__root__

    def visit(
        self,
        building_executor: typing.Callable[[BuildingExecutorResponse], T_Result],
        running: typing.Callable[[RunningResponse], T_Result],
        errored: typing.Callable[[ErroredResponse], T_Result],
        stopped: typing.Callable[[StoppedResponse], T_Result],
        graded: typing.Callable[[GradedResponse], T_Result],
        graded_v_2: typing.Callable[[GradedResponseV2], T_Result],
        workspace_ran: typing.Callable[[WorkspaceRanResponse], T_Result],
        recording: typing.Callable[[RecordingResponseNotification], T_Result],
        recorded: typing.Callable[[RecordedResponseNotification], T_Result],
        invalid_request: typing.Callable[[InvalidRequestResponse], T_Result],
        finished: typing.Callable[[FinishedResponse], T_Result],
    ) -> T_Result:
        unioned_value = self.get_as_union()
        if unioned_value.type == "buildingExecutor":
            return building_executor(
                BuildingExecutorResponse(**unioned_value.dict(exclude_unset=True, exclude={"type"}))
            )
        if unioned_value.type == "running":
            return running(RunningResponse(**unioned_value.dict(exclude_unset=True, exclude={"type"})))
        if unioned_value.type == "errored":
            return errored(ErroredResponse(**unioned_value.dict(exclude_unset=True, exclude={"type"})))
        if unioned_value.type == "stopped":
            return stopped(StoppedResponse(**unioned_value.dict(exclude_unset=True, exclude={"type"})))
        if unioned_value.type == "graded":
            return graded(GradedResponse(**unioned_value.dict(exclude_unset=True, exclude={"type"})))
        if unioned_value.type == "gradedV2":
            return graded_v_2(GradedResponseV2(**unioned_value.dict(exclude_unset=True, exclude={"type"})))
        if unioned_value.type == "workspaceRan":
            return workspace_ran(WorkspaceRanResponse(**unioned_value.dict(exclude_unset=True, exclude={"type"})))
        if unioned_value.type == "recording":
            return recording(RecordingResponseNotification(**unioned_value.dict(exclude_unset=True, exclude={"type"})))
        if unioned_value.type == "recorded":
            return recorded(RecordedResponseNotification(**unioned_value.dict(exclude_unset=True, exclude={"type"})))
        if unioned_value.type == "invalidRequest":
            return invalid_request(InvalidRequestResponse(**unioned_value.dict(exclude_unset=True, exclude={"type"})))
        if unioned_value.type == "finished":
            return finished(FinishedResponse(**unioned_value.dict(exclude_unset=True, exclude={"type"})))


class _CodeExecutionUpdate:
    class BuildingExecutor(BuildingExecutorResponse):
        type: typing.Literal["buildingExecutor"] = "buildingExecutor"

    class Running(RunningResponse):
        type: typing.Literal["running"] = "running"

    class Errored(ErroredResponse):
        type: typing.Literal["errored"] = "errored"

    class Stopped(StoppedResponse):
        type: typing.Literal["stopped"] = "stopped"

    class Graded(GradedResponse):
        type: typing.Literal["graded"] = "graded"

    class GradedV2(GradedResponseV2):
        type: typing.Literal["gradedV2"] = "gradedV2"

    class WorkspaceRan(WorkspaceRanResponse):
        type: typing.Literal["workspaceRan"] = "workspaceRan"

    class Recording(RecordingResponseNotification):
        type: typing.Literal["recording"] = "recording"

    class Recorded(RecordedResponseNotification):
        type: typing.Literal["recorded"] = "recorded"

    class InvalidRequest(InvalidRequestResponse):
        type: typing.Literal["invalidRequest"] = "invalidRequest"

    class Finished(FinishedResponse):
        type: typing.Literal["finished"] = "finished"
