# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .test_submission_state import TestSubmissionState
from .workspace_submission_state import WorkspaceSubmissionState


class SubmissionTypeState_Test(TestSubmissionState):
    type: typing.Literal["test"]
    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
class SubmissionTypeState_Workspace(WorkspaceSubmissionState):
    type: typing.Literal["workspace"]
    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
SubmissionTypeState = typing.Union[SubmissionTypeState_Test, SubmissionTypeState_Workspace]
