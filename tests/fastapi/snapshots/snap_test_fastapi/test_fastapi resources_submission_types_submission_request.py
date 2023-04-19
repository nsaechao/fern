# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .initialize_problem_request import (
    InitializeProblemRequest as resources_submission_types_initialize_problem_request_InitializeProblemRequest,
)
from .stop_request import StopRequest
from .submit_request_v_2 import SubmitRequestV2
from .workspace_submit_request import WorkspaceSubmitRequest

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def initialize_problem_request(
        self, value: resources_submission_types_initialize_problem_request_InitializeProblemRequest
    ) -> SubmissionRequest:
        return SubmissionRequest(
            __root__=_SubmissionRequest.InitializeProblemRequest(
                **value.dict(exclude_unset=True), type="initializeProblemRequest"
            )
        )

    def initialize_workspace_request(self) -> SubmissionRequest:
        return SubmissionRequest(
            __root__=_SubmissionRequest.InitializeWorkspaceRequest(type="initializeWorkspaceRequest")
        )

    def submit_v_2(self, value: SubmitRequestV2) -> SubmissionRequest:
        return SubmissionRequest(
            __root__=_SubmissionRequest.SubmitV2(**value.dict(exclude_unset=True), type="submitV2")
        )

    def workspace_submit(self, value: WorkspaceSubmitRequest) -> SubmissionRequest:
        return SubmissionRequest(
            __root__=_SubmissionRequest.WorkspaceSubmit(**value.dict(exclude_unset=True), type="workspaceSubmit")
        )

    def stop(self, value: StopRequest) -> SubmissionRequest:
        return SubmissionRequest(__root__=_SubmissionRequest.Stop(**value.dict(exclude_unset=True), type="stop"))


class SubmissionRequest(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(
        self,
    ) -> typing.Union[
        _SubmissionRequest.InitializeProblemRequest,
        _SubmissionRequest.InitializeWorkspaceRequest,
        _SubmissionRequest.SubmitV2,
        _SubmissionRequest.WorkspaceSubmit,
        _SubmissionRequest.Stop,
    ]:
        return self.__root__

    def visit(
        self,
        initialize_problem_request: typing.Callable[
            [resources_submission_types_initialize_problem_request_InitializeProblemRequest], T_Result
        ],
        initialize_workspace_request: typing.Callable[[], T_Result],
        submit_v_2: typing.Callable[[SubmitRequestV2], T_Result],
        workspace_submit: typing.Callable[[WorkspaceSubmitRequest], T_Result],
        stop: typing.Callable[[StopRequest], T_Result],
    ) -> T_Result:
        if self.__root__.type == "initializeProblemRequest":
            return initialize_problem_request(self.__root__)
        if self.__root__.type == "initializeWorkspaceRequest":
            return initialize_workspace_request()
        if self.__root__.type == "submitV2":
            return submit_v_2(self.__root__)
        if self.__root__.type == "workspaceSubmit":
            return workspace_submit(self.__root__)
        if self.__root__.type == "stop":
            return stop(self.__root__)

    __root__: typing_extensions.Annotated[
        typing.Union[
            _SubmissionRequest.InitializeProblemRequest,
            _SubmissionRequest.InitializeWorkspaceRequest,
            _SubmissionRequest.SubmitV2,
            _SubmissionRequest.WorkspaceSubmit,
            _SubmissionRequest.Stop,
        ],
        pydantic.Field(discriminator="type"),
    ]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @SubmissionRequest.Validators.validate
            def validate(value: typing.Union[_SubmissionRequest.InitializeProblemRequest, _SubmissionRequest.InitializeWorkspaceRequest, _SubmissionRequest.SubmitV2, _SubmissionRequest.WorkspaceSubmit, _SubmissionRequest.Stop]) -> typing.Union[_SubmissionRequest.InitializeProblemRequest, _SubmissionRequest.InitializeWorkspaceRequest, _SubmissionRequest.SubmitV2, _SubmissionRequest.WorkspaceSubmit, _SubmissionRequest.Stop]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [
                        typing.Union[
                            _SubmissionRequest.InitializeProblemRequest,
                            _SubmissionRequest.InitializeWorkspaceRequest,
                            _SubmissionRequest.SubmitV2,
                            _SubmissionRequest.WorkspaceSubmit,
                            _SubmissionRequest.Stop,
                        ]
                    ],
                    typing.Union[
                        _SubmissionRequest.InitializeProblemRequest,
                        _SubmissionRequest.InitializeWorkspaceRequest,
                        _SubmissionRequest.SubmitV2,
                        _SubmissionRequest.WorkspaceSubmit,
                        _SubmissionRequest.Stop,
                    ],
                ]
            ]
        ] = []

        @classmethod
        def validate(
            cls,
            validator: typing.Callable[
                [
                    typing.Union[
                        _SubmissionRequest.InitializeProblemRequest,
                        _SubmissionRequest.InitializeWorkspaceRequest,
                        _SubmissionRequest.SubmitV2,
                        _SubmissionRequest.WorkspaceSubmit,
                        _SubmissionRequest.Stop,
                    ]
                ],
                typing.Union[
                    _SubmissionRequest.InitializeProblemRequest,
                    _SubmissionRequest.InitializeWorkspaceRequest,
                    _SubmissionRequest.SubmitV2,
                    _SubmissionRequest.WorkspaceSubmit,
                    _SubmissionRequest.Stop,
                ],
            ],
        ) -> None:
            cls._validators.append(validator)

    @pydantic.root_validator(pre=False)
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(
            typing.Union[
                _SubmissionRequest.InitializeProblemRequest,
                _SubmissionRequest.InitializeWorkspaceRequest,
                _SubmissionRequest.SubmitV2,
                _SubmissionRequest.WorkspaceSubmit,
                _SubmissionRequest.Stop,
            ],
            values.get("__root__"),
        )
        for validator in SubmissionRequest.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


class _SubmissionRequest:
    class InitializeProblemRequest(resources_submission_types_initialize_problem_request_InitializeProblemRequest):
        type: typing_extensions.Literal["initializeProblemRequest"]

        class Config:
            allow_population_by_field_name = True

    class InitializeWorkspaceRequest(pydantic.BaseModel):
        type: typing_extensions.Literal["initializeWorkspaceRequest"]

    class SubmitV2(SubmitRequestV2):
        type: typing_extensions.Literal["submitV2"]

        class Config:
            allow_population_by_field_name = True

    class WorkspaceSubmit(WorkspaceSubmitRequest):
        type: typing_extensions.Literal["workspaceSubmit"]

        class Config:
            allow_population_by_field_name = True

    class Stop(StopRequest):
        type: typing_extensions.Literal["stop"]

        class Config:
            allow_population_by_field_name = True


SubmissionRequest.update_forward_refs()
