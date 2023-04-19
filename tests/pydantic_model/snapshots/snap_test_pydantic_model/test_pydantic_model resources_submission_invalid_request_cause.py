# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .custom_test_cases_unsupported import CustomTestCasesUnsupported
from .submission_id_not_found import SubmissionIdNotFound
from .unexpected_language_error import UnexpectedLanguageError


class InvalidRequestCause_SubmissionIdNotFound(SubmissionIdNotFound):
    type: typing_extensions.Literal["submissionIdNotFound"]

    class Config:
        allow_population_by_field_name = True


class InvalidRequestCause_CustomTestCasesUnsupported(CustomTestCasesUnsupported):
    type: typing_extensions.Literal["customTestCasesUnsupported"]

    class Config:
        allow_population_by_field_name = True


class InvalidRequestCause_UnexpectedLanguage(UnexpectedLanguageError):
    type: typing_extensions.Literal["unexpectedLanguage"]

    class Config:
        allow_population_by_field_name = True


InvalidRequestCause = typing_extensions.Annotated[
    typing.Union[
        InvalidRequestCause_SubmissionIdNotFound,
        InvalidRequestCause_CustomTestCasesUnsupported,
        InvalidRequestCause_UnexpectedLanguage,
    ],
    pydantic.Field(discriminator="type"),
]
