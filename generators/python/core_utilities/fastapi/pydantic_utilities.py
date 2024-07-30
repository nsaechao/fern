# nopycln: file
import datetime as dt
import typing
from collections import defaultdict
from functools import wraps

import pydantic

from .datetime_utils import serialize_datetime

IS_PYDANTIC_V2 = pydantic.VERSION.startswith("2.")

if IS_PYDANTIC_V2:
    # isort will try to reformat the comments on these imports, which breaks mypy
    # isort: off
    from pydantic.v1.datetime_parse import (  # type: ignore # pyright: ignore[reportMissingImports] # Pydantic v2
        parse_date as parse_date,
    )
    from pydantic.v1.datetime_parse import (  # pyright: ignore[reportMissingImports] # Pydantic v2
        parse_datetime as parse_datetime,
    )
    from pydantic.v1.json import (  # type: ignore # pyright: ignore[reportMissingImports] # Pydantic v2
        ENCODERS_BY_TYPE as encoders_by_type,
    )
    from pydantic.v1.typing import (  # type: ignore # pyright: ignore[reportMissingImports] # Pydantic v2
        get_args as get_args,
    )
    from pydantic.v1.typing import (  # pyright: ignore[reportMissingImports] # Pydantic v2
        get_origin as get_origin,
    )
    from pydantic.v1.typing import (  # pyright: ignore[reportMissingImports] # Pydantic v2
        is_literal_type as is_literal_type,
    )
    from pydantic.v1.typing import (  # pyright: ignore[reportMissingImports] # Pydantic v2
        is_union as is_union,
    )
    from pydantic.v1.fields import ModelField as ModelField  # type: ignore # pyright: ignore[reportMissingImports] # Pydantic v2
else:
    from pydantic.datetime_parse import parse_date as parse_date  # type: ignore # Pydantic v1
    from pydantic.datetime_parse import parse_datetime as parse_datetime  # type: ignore # Pydantic v1
    from pydantic.fields import ModelField as ModelField  # type: ignore # Pydantic v1
    from pydantic.json import ENCODERS_BY_TYPE as encoders_by_type  # type: ignore # Pydantic v1
    from pydantic.typing import get_args as get_args  # type: ignore # Pydantic v1
    from pydantic.typing import get_origin as get_origin  # type: ignore # Pydantic v1
    from pydantic.typing import is_literal_type as is_literal_type  # type: ignore # Pydantic v1
    from pydantic.typing import is_union as is_union  # type: ignore # Pydantic v1

    # isort: on


T = typing.TypeVar("T")
Model = typing.TypeVar("Model", bound=pydantic.BaseModel)


def deep_union_pydantic_dicts(
    source: typing.Dict[str, typing.Any], destination: typing.Dict[str, typing.Any]
) -> typing.Dict[str, typing.Any]:
    for key, value in source.items():
        if isinstance(value, dict):
            node = destination.setdefault(key, {})
            deep_union_pydantic_dicts(value, node)
        else:
            destination[key] = value

    return destination


def parse_obj_as(type_: typing.Type[T], object_: typing.Any) -> T:
    if IS_PYDANTIC_V2:
        adapter = pydantic.TypeAdapter(type_)  # type: ignore # Pydantic v2
        return adapter.validate_python(object_)
    else:
        return pydantic.parse_obj_as(type_, object_)


def to_jsonable_with_fallback(
    obj: typing.Any, fallback_serializer: typing.Callable[[typing.Any], typing.Any]
) -> typing.Any:
    if IS_PYDANTIC_V2:
        from pydantic_core import to_jsonable_python

        return to_jsonable_python(obj, fallback=fallback_serializer)
    else:
        return fallback_serializer(obj)


class UniversalBaseModel(pydantic.BaseModel):

    # # Here we apply both Pydantic V1 and V2 configurations, certain versions of mypy do not respect `allow_population_by_field_name` when applied conditionally.
    # class Config:
    #     populate_by_name = True
    #     smart_union = True # type: ignore # Pydantic error with mypy not recognizing the config if applied conditionally
    #     allow_population_by_field_name = True  # type: ignore # Pydantic error with mypy not recognizing the config if applied conditionally
    #     json_encoders = {dt.datetime: serialize_datetime}

    if IS_PYDANTIC_V2:
        # Allow fields begining with `model_` to be used in the model
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(protected_namespaces=(), populate_by_name=True, json_encoders={dt.datetime: serialize_datetime})  # type: ignore # Pydantic v2
    else:
        class Config:
            smart_union = True # type: ignore # Pydantic error with mypy not recognizing the config if applied conditionally
            allow_population_by_field_name = True  # type: ignore # Pydantic error with mypy not recognizing the config if applied conditionally
            json_encoders = {dt.datetime: serialize_datetime}

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        if IS_PYDANTIC_V2:
            return super().model_dump_json(**kwargs_with_defaults)  # type: ignore # Pydantic v2
        else:
            return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        if IS_PYDANTIC_V2:
            return deep_union_pydantic_dicts(
                super().model_dump(**kwargs_with_defaults_exclude_unset),  # type: ignore # Pydantic v2
                super().model_dump(**kwargs_with_defaults_exclude_none),  # type: ignore # Pydantic v2
            )
        else:
            return deep_union_pydantic_dicts(
                super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
            )


UniversalRootModel: typing.Type[typing.Any]
if IS_PYDANTIC_V2:

    class V2RootModel(UniversalBaseModel, pydantic.RootModel):  # type: ignore # Pydantic v2
        pass

    UniversalRootModel = V2RootModel
else:
    UniversalRootModel = UniversalBaseModel


def encode_by_type(o: typing.Any) -> typing.Any:
    encoders_by_class_tuples: typing.Dict[
        typing.Callable[[typing.Any], typing.Any], typing.Tuple[typing.Any, ...]
    ] = defaultdict(tuple)
    for type_, encoder in encoders_by_type.items():
        encoders_by_class_tuples[encoder] += (type_,)

    if type(o) in encoders_by_type:
        return encoders_by_type[type(o)](o)
    for encoder, classes_tuple in encoders_by_class_tuples.items():
        if isinstance(o, classes_tuple):
            return encoder(o)


def update_forward_refs(model: typing.Type["Model"], **localns: typing.Any) -> None:
    if IS_PYDANTIC_V2:
        model.model_rebuild(force=True, raise_errors=False)  # type: ignore # Pydantic v2
    else:
        model.update_forward_refs(**localns)


# Mirrors Pydantic's internal typing
AnyCallable = typing.Callable[..., typing.Any]


def universal_root_validator(pre: bool = False) -> typing.Callable[[AnyCallable], AnyCallable]:
    def decorator(func: AnyCallable) -> AnyCallable:
        @wraps(func)
        def validate(*args: typing.Any, **kwargs: typing.Any) -> AnyCallable:
            if IS_PYDANTIC_V2:
                wrapped_func = pydantic.model_validator("before" if pre else "after")(func)  # type: ignore # Pydantic v2
            else:
                wrapped_func = pydantic.root_validator(pre=pre)(func)  # type: ignore # Pydantic v1

            return wrapped_func(*args, **kwargs)

        return validate

    return decorator


def universal_field_validator(field_name: str, pre: bool = False) -> typing.Callable[[AnyCallable], AnyCallable]:
    def decorator(func: AnyCallable) -> AnyCallable:
        @wraps(func)
        def validate(*args: typing.Any, **kwargs: typing.Any) -> AnyCallable:
            if IS_PYDANTIC_V2:
                wrapped_func = pydantic.field_validator(field_name, mode="before" if pre else "after")(func)  # type: ignore # Pydantic v2
            else:
                wrapped_func = pydantic.validator(field_name, pre=pre)(func)

            return wrapped_func(*args, **kwargs)

        return validate

    return decorator
