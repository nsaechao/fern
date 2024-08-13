# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from .running_submission_state import RunningSubmissionState
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from .error_info import ErrorInfo
from .graded_test_case_update import GradedTestCaseUpdate
from .recorded_test_case_update import RecordedTestCaseUpdate
from ....core.pydantic_utilities import UniversalRootModel
import typing
import typing_extensions
import pydantic
from ....core.pydantic_utilities import UniversalBaseModel
from ....core.pydantic_utilities import update_forward_refs

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def running(self, value: RunningSubmissionState) -> TestSubmissionUpdateInfo:
        if IS_PYDANTIC_V2:
            return TestSubmissionUpdateInfo(
                root=_TestSubmissionUpdateInfo.Running(type="running", value=value)
            )  # type: ignore
        else:
            return TestSubmissionUpdateInfo(
                __root__=_TestSubmissionUpdateInfo.Running(type="running", value=value)
            )  # type: ignore

    def stopped(self) -> TestSubmissionUpdateInfo:
        if IS_PYDANTIC_V2:
            return TestSubmissionUpdateInfo(
                root=_TestSubmissionUpdateInfo.Stopped(type="stopped")
            )  # type: ignore
        else:
            return TestSubmissionUpdateInfo(
                __root__=_TestSubmissionUpdateInfo.Stopped(type="stopped")
            )  # type: ignore

    def errored(self, value: ErrorInfo) -> TestSubmissionUpdateInfo:
        if IS_PYDANTIC_V2:
            return TestSubmissionUpdateInfo(
                root=_TestSubmissionUpdateInfo.Errored(type="errored", value=value)
            )  # type: ignore
        else:
            return TestSubmissionUpdateInfo(
                __root__=_TestSubmissionUpdateInfo.Errored(type="errored", value=value)
            )  # type: ignore

    def graded_test_case(self, value: GradedTestCaseUpdate) -> TestSubmissionUpdateInfo:
        if IS_PYDANTIC_V2:
            return TestSubmissionUpdateInfo(
                root=_TestSubmissionUpdateInfo.GradedTestCase(
                    **value.dict(exclude_unset=True), type="gradedTestCase"
                )
            )  # type: ignore
        else:
            return TestSubmissionUpdateInfo(
                __root__=_TestSubmissionUpdateInfo.GradedTestCase(
                    **value.dict(exclude_unset=True), type="gradedTestCase"
                )
            )  # type: ignore

    def recorded_test_case(
        self, value: RecordedTestCaseUpdate
    ) -> TestSubmissionUpdateInfo:
        if IS_PYDANTIC_V2:
            return TestSubmissionUpdateInfo(
                root=_TestSubmissionUpdateInfo.RecordedTestCase(
                    **value.dict(exclude_unset=True), type="recordedTestCase"
                )
            )  # type: ignore
        else:
            return TestSubmissionUpdateInfo(
                __root__=_TestSubmissionUpdateInfo.RecordedTestCase(
                    **value.dict(exclude_unset=True), type="recordedTestCase"
                )
            )  # type: ignore

    def finished(self) -> TestSubmissionUpdateInfo:
        if IS_PYDANTIC_V2:
            return TestSubmissionUpdateInfo(
                root=_TestSubmissionUpdateInfo.Finished(type="finished")
            )  # type: ignore
        else:
            return TestSubmissionUpdateInfo(
                __root__=_TestSubmissionUpdateInfo.Finished(type="finished")
            )  # type: ignore


class TestSubmissionUpdateInfo(UniversalRootModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    if IS_PYDANTIC_V2:
        root: typing_extensions.Annotated[
            typing.Union[
                _TestSubmissionUpdateInfo.Running,
                _TestSubmissionUpdateInfo.Stopped,
                _TestSubmissionUpdateInfo.Errored,
                _TestSubmissionUpdateInfo.GradedTestCase,
                _TestSubmissionUpdateInfo.RecordedTestCase,
                _TestSubmissionUpdateInfo.Finished,
            ],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(
            self,
        ) -> typing.Union[
            _TestSubmissionUpdateInfo.Running,
            _TestSubmissionUpdateInfo.Stopped,
            _TestSubmissionUpdateInfo.Errored,
            _TestSubmissionUpdateInfo.GradedTestCase,
            _TestSubmissionUpdateInfo.RecordedTestCase,
            _TestSubmissionUpdateInfo.Finished,
        ]:
            return self.root
    else:
        __root__: typing_extensions.Annotated[
            typing.Union[
                _TestSubmissionUpdateInfo.Running,
                _TestSubmissionUpdateInfo.Stopped,
                _TestSubmissionUpdateInfo.Errored,
                _TestSubmissionUpdateInfo.GradedTestCase,
                _TestSubmissionUpdateInfo.RecordedTestCase,
                _TestSubmissionUpdateInfo.Finished,
            ],
            pydantic.Field(discriminator="type"),
        ]

        def get_as_union(
            self,
        ) -> typing.Union[
            _TestSubmissionUpdateInfo.Running,
            _TestSubmissionUpdateInfo.Stopped,
            _TestSubmissionUpdateInfo.Errored,
            _TestSubmissionUpdateInfo.GradedTestCase,
            _TestSubmissionUpdateInfo.RecordedTestCase,
            _TestSubmissionUpdateInfo.Finished,
        ]:
            return self.__root__

    def visit(
        self,
        running: typing.Callable[[RunningSubmissionState], T_Result],
        stopped: typing.Callable[[], T_Result],
        errored: typing.Callable[[ErrorInfo], T_Result],
        graded_test_case: typing.Callable[[GradedTestCaseUpdate], T_Result],
        recorded_test_case: typing.Callable[[RecordedTestCaseUpdate], T_Result],
        finished: typing.Callable[[], T_Result],
    ) -> T_Result:
        unioned_value = self.get_as_union()
        if unioned_value.type == "running":
            return running(unioned_value.value)
        if unioned_value.type == "stopped":
            return stopped()
        if unioned_value.type == "errored":
            return errored(unioned_value.value)
        if unioned_value.type == "gradedTestCase":
            return graded_test_case(
                GradedTestCaseUpdate(
                    **unioned_value.dict(exclude_unset=True, exclude={"type"})
                )
            )
        if unioned_value.type == "recordedTestCase":
            return recorded_test_case(
                RecordedTestCaseUpdate(
                    **unioned_value.dict(exclude_unset=True, exclude={"type"})
                )
            )
        if unioned_value.type == "finished":
            return finished()


class _TestSubmissionUpdateInfo:
    class Running(UniversalBaseModel):
        type: typing.Literal["running"] = "running"
        value: RunningSubmissionState

    class Stopped(UniversalBaseModel):
        type: typing.Literal["stopped"] = "stopped"

    class Errored(UniversalBaseModel):
        type: typing.Literal["errored"] = "errored"
        value: ErrorInfo

    class GradedTestCase(GradedTestCaseUpdate):
        type: typing.Literal["gradedTestCase"] = "gradedTestCase"

    class RecordedTestCase(RecordedTestCaseUpdate):
        type: typing.Literal["recordedTestCase"] = "recordedTestCase"

    class Finished(UniversalBaseModel):
        type: typing.Literal["finished"] = "finished"


update_forward_refs(TestSubmissionUpdateInfo)
