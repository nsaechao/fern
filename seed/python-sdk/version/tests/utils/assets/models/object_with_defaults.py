# This file was auto-generated by Fern from our API Definition.

# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions


class ObjectWithDefaultsParams(typing_extensions.TypedDict):
    """
    Defines properties with default values and validation rules.
    """

    decimal: typing_extensions.NotRequired[float]
    string: typing_extensions.NotRequired[str]
    required_string: str
