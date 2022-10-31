# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...commons.types.language import Language
from .submission_type_state import SubmissionTypeState


class GetSubmissionStateResponse(pydantic.BaseModel):
    time_submitted: typing.Optional[dt.datetime] = pydantic.Field(alias="timeSubmitted")
    submission: str
    language: Language
    submission_type_state: SubmissionTypeState = pydantic.Field(alias="submissionTypeState")

    class Partial(typing_extensions.TypedDict):
        time_submitted: typing_extensions.NotRequired[typing.Optional[dt.datetime]]
        submission: typing_extensions.NotRequired[str]
        language: typing_extensions.NotRequired[Language]
        submission_type_state: typing_extensions.NotRequired[SubmissionTypeState]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GetSubmissionStateResponse.Validators.root
            def validate(values: GetSubmissionStateResponse.Partial) -> GetSubmissionStateResponse.Partial:
                ...

            @GetSubmissionStateResponse.Validators.field("time_submitted")
            def validate_time_submitted(v: typing.Optional[dt.datetime], values: GetSubmissionStateResponse.Partial) -> typing.Optional[dt.datetime]:
                ...

            @GetSubmissionStateResponse.Validators.field("submission")
            def validate_submission(v: str, values: GetSubmissionStateResponse.Partial) -> str:
                ...

            @GetSubmissionStateResponse.Validators.field("language")
            def validate_language(v: Language, values: GetSubmissionStateResponse.Partial) -> Language:
                ...

            @GetSubmissionStateResponse.Validators.field("submission_type_state")
            def validate_submission_type_state(v: SubmissionTypeState, values: GetSubmissionStateResponse.Partial) -> SubmissionTypeState:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[GetSubmissionStateResponse.Partial], GetSubmissionStateResponse.Partial]]
        ] = []
        _time_submitted_validators: typing.ClassVar[
            typing.List[GetSubmissionStateResponse.Validators.TimeSubmittedValidator]
        ] = []
        _submission_validators: typing.ClassVar[
            typing.List[GetSubmissionStateResponse.Validators.SubmissionValidator]
        ] = []
        _language_validators: typing.ClassVar[typing.List[GetSubmissionStateResponse.Validators.LanguageValidator]] = []
        _submission_type_state_validators: typing.ClassVar[
            typing.List[GetSubmissionStateResponse.Validators.SubmissionTypeStateValidator]
        ] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[GetSubmissionStateResponse.Partial], GetSubmissionStateResponse.Partial]
        ) -> typing.Callable[[GetSubmissionStateResponse.Partial], GetSubmissionStateResponse.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["time_submitted"]
        ) -> typing.Callable[
            [GetSubmissionStateResponse.Validators.TimeSubmittedValidator],
            GetSubmissionStateResponse.Validators.TimeSubmittedValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission"]
        ) -> typing.Callable[
            [GetSubmissionStateResponse.Validators.SubmissionValidator],
            GetSubmissionStateResponse.Validators.SubmissionValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["language"]
        ) -> typing.Callable[
            [GetSubmissionStateResponse.Validators.LanguageValidator],
            GetSubmissionStateResponse.Validators.LanguageValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_type_state"]
        ) -> typing.Callable[
            [GetSubmissionStateResponse.Validators.SubmissionTypeStateValidator],
            GetSubmissionStateResponse.Validators.SubmissionTypeStateValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "time_submitted":
                    cls._time_submitted_validators.append(validator)
                if field_name == "submission":
                    cls._submission_validators.append(validator)
                if field_name == "language":
                    cls._language_validators.append(validator)
                if field_name == "submission_type_state":
                    cls._submission_type_state_validators.append(validator)
                return validator

            return decorator

        class TimeSubmittedValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Optional[dt.datetime], *, values: GetSubmissionStateResponse.Partial
            ) -> typing.Optional[dt.datetime]:
                ...

        class SubmissionValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: GetSubmissionStateResponse.Partial) -> str:
                ...

        class LanguageValidator(typing_extensions.Protocol):
            def __call__(self, v: Language, *, values: GetSubmissionStateResponse.Partial) -> Language:
                ...

        class SubmissionTypeStateValidator(typing_extensions.Protocol):
            def __call__(
                self, v: SubmissionTypeState, *, values: GetSubmissionStateResponse.Partial
            ) -> SubmissionTypeState:
                ...

    @pydantic.root_validator
    def _validate(cls, values: GetSubmissionStateResponse.Partial) -> GetSubmissionStateResponse.Partial:
        for validator in GetSubmissionStateResponse.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("time_submitted")
    def _validate_time_submitted(
        cls, v: typing.Optional[dt.datetime], values: GetSubmissionStateResponse.Partial
    ) -> typing.Optional[dt.datetime]:
        for validator in GetSubmissionStateResponse.Validators._time_submitted_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("submission")
    def _validate_submission(cls, v: str, values: GetSubmissionStateResponse.Partial) -> str:
        for validator in GetSubmissionStateResponse.Validators._submission_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("language")
    def _validate_language(cls, v: Language, values: GetSubmissionStateResponse.Partial) -> Language:
        for validator in GetSubmissionStateResponse.Validators._language_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("submission_type_state")
    def _validate_submission_type_state(
        cls, v: SubmissionTypeState, values: GetSubmissionStateResponse.Partial
    ) -> SubmissionTypeState:
        for validator in GetSubmissionStateResponse.Validators._submission_type_state_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
