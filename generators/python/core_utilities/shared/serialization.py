import collections
import inspect
import typing

import typing_extensions

import pydantic


class FieldMetadata:
    """
    Metadata class used to annotate fields to provide additional information.

    Example:
    class MyDict(TypedDict):
        field: typing.Annotated[str, FieldMetadata(alias="field_name")]

    Will serialize: `{"field": "value"}`
    To: `{"field_name": "value"}`
    """

    alias: str

    def __init__(self, *, alias: str) -> None:
        self.alias = alias


def convert_and_respect_annotation_metadata(
    *,
    object_: typing.Any,
    annotation: typing.Any,
    inner_type: typing.Optional[typing.Any] = None,
    direction: typing.Literal["read", "write"],
) -> typing.Any:
    """
    Respect the metadata annotations on a field, such as aliasing. This function effectively
    manipulates the dict-form of an object to respect the metadata annotations. This is primarily used for
    TypedDicts, which cannot support aliasing out of the box, and can be extended for additional
    utilities, such as defaults.

    Parameters
    ----------
    object_ : typing.Any

    annotation : type
        The type we're looking to apply typing annotations from

    inner_type : typing.Optional[type]

    Returns
    -------
    typing.Any
    """

    if object_ is None:
        return None
    if inner_type is None:
        inner_type = annotation

    clean_type = _remove_annotations(inner_type)
    # Pydantic models
    if (
        inspect.isclass(clean_type)
        and issubclass(clean_type, pydantic.BaseModel)
        and isinstance(object_, typing.Mapping)
    ):
        return _convert_mapping(object_, clean_type, direction)
    # TypedDicts
    if typing_extensions.is_typeddict(clean_type) and isinstance(object_, typing.Mapping):
        return _convert_mapping(object_, clean_type, direction)

    if (
        typing_extensions.get_origin(clean_type) == typing.Dict
        or typing_extensions.get_origin(clean_type) == dict
        or clean_type == typing.Dict
    ) and isinstance(object_, typing.Dict):
        key_type = typing_extensions.get_args(clean_type)[0]
        value_type = typing_extensions.get_args(clean_type)[1]

        return {
            key: convert_and_respect_annotation_metadata(
                object_=value,
                annotation=annotation,
                inner_type=value_type,
                direction=direction,
            )
            for key, value in object_.items()
        }

    # If you're iterating on a string, do not bother to coerce it to a sequence.
    if not isinstance(object_, str):
        if (
            typing_extensions.get_origin(clean_type) == typing.Set
            or typing_extensions.get_origin(clean_type) == set
            or clean_type == typing.Set
        ) and isinstance(object_, typing.Set):
            inner_type = typing_extensions.get_args(clean_type)[0]
            return {
                convert_and_respect_annotation_metadata(
                    object_=item,
                    annotation=annotation,
                    inner_type=inner_type,
                    direction=direction,
                )
                for item in object_
            }
        elif (
            (
                typing_extensions.get_origin(clean_type) == typing.List
                or typing_extensions.get_origin(clean_type) == list
                or clean_type == typing.List
            )
            and isinstance(object_, typing.List)
        ) or (
            (
                typing_extensions.get_origin(clean_type) == typing.Sequence
                or typing_extensions.get_origin(clean_type) == collections.abc.Sequence
                or clean_type == typing.Sequence
            )
            and isinstance(object_, typing.Sequence)
        ):
            inner_type = typing_extensions.get_args(clean_type)[0]
            return [
                convert_and_respect_annotation_metadata(
                    object_=item,
                    annotation=annotation,
                    inner_type=inner_type,
                    direction=direction,
                )
                for item in object_
            ]

    if typing_extensions.get_origin(clean_type) == typing.Union:
        # We should be able to ~relatively~ safely try to convert keys against all
        # member types in the union, the edge case here is if one member aliases a field
        # of the same name to a different name from another member
        # Or if another member aliases a field of the same name that another member does not.
        for member in typing_extensions.get_args(clean_type):
            object_ = convert_and_respect_annotation_metadata(
                object_=object_,
                annotation=annotation,
                inner_type=member,
                direction=direction,
            )
        return object_

    annotated_type = _get_annotation(annotation)
    if annotated_type is None:
        return object_

    # If the object is not a TypedDict, a Union, or other container (list, set, sequence, etc.)
    # Then we can safely call it on the recursive conversion.
    return object_


def _convert_mapping(
    object_: typing.Mapping[str, object],
    expected_type: typing.Any,
    direction: typing.Literal["read", "write"],
) -> typing.Mapping[str, object]:
    converted_object: typing.Dict[str, object] = {}
    annotations = typing_extensions.get_type_hints(expected_type, include_extras=True)
    aliases_to_field_names = _get_alias_to_field_name(annotations)
    for key, value in object_.items():
        if direction == "read" and key in aliases_to_field_names:
            dealiased_key = aliases_to_field_names.get(key)
            if dealiased_key is not None:
                type_ = annotations.get(dealiased_key)
        else:
            type_ = annotations.get(key)
        # Note you can't get the annotation by the field name if you're in read mode, so you must check the aliases map
        #
        # So this is effectively saying if we're in write mode, and we don't have a type, or if we're in read mode and we don't have an alias
        # then we can just pass the value through as is
        if type_ is None:
            converted_object[key] = value
        elif direction == "read" and key not in aliases_to_field_names:
            converted_object[key] = convert_and_respect_annotation_metadata(
                object_=value, annotation=type_, direction=direction
            )
        else:
            converted_object[
                _alias_key(key, type_, direction, aliases_to_field_names)
            ] = convert_and_respect_annotation_metadata(object_=value, annotation=type_, direction=direction)
    return converted_object


def _get_annotation(type_: typing.Any) -> typing.Optional[typing.Any]:
    maybe_annotated_type = typing_extensions.get_origin(type_)
    if maybe_annotated_type is None:
        return None

    if maybe_annotated_type == typing_extensions.NotRequired:
        type_ = typing_extensions.get_args(type_)[0]
        maybe_annotated_type = typing_extensions.get_origin(type_)

    if maybe_annotated_type == typing_extensions.Annotated:
        return type_

    return None


def _remove_annotations(type_: typing.Any) -> typing.Any:
    maybe_annotated_type = typing_extensions.get_origin(type_)
    if maybe_annotated_type is None:
        return type_

    if maybe_annotated_type == typing_extensions.NotRequired:
        return _remove_annotations(typing_extensions.get_args(type_)[0])

    if maybe_annotated_type == typing_extensions.Annotated:
        return _remove_annotations(typing_extensions.get_args(type_)[0])

    return type_


def get_alias_to_field_mapping(type_: typing.Any) -> typing.Dict[str, str]:
    annotations = typing_extensions.get_type_hints(type_, include_extras=True)
    return _get_alias_to_field_name(annotations)


def get_field_to_alias_mapping(type_: typing.Any) -> typing.Dict[str, str]:
    annotations = typing_extensions.get_type_hints(type_, include_extras=True)
    return _get_field_to_alias_name(annotations)


def _get_alias_to_field_name(
    field_to_hint: typing.Dict[str, typing.Any],
) -> typing.Dict[str, str]:
    aliases = {}
    for field, hint in field_to_hint.items():
        maybe_alias = _get_alias_from_type(hint)
        if maybe_alias is not None:
            aliases[maybe_alias] = field
    return aliases


def _get_field_to_alias_name(
    field_to_hint: typing.Dict[str, typing.Any],
) -> typing.Dict[str, str]:
    aliases = {}
    for field, hint in field_to_hint.items():
        maybe_alias = _get_alias_from_type(hint)
        if maybe_alias is not None:
            aliases[field] = maybe_alias
    return aliases


def _get_alias_from_type(type_: typing.Any) -> typing.Optional[str]:
    maybe_annotated_type = _get_annotation(type_)

    if maybe_annotated_type is not None:
        # The actual annotations are 1 onward, the first is the annotated type
        annotations = typing_extensions.get_args(maybe_annotated_type)[1:]

        for annotation in annotations:
            if isinstance(annotation, FieldMetadata) and annotation.alias is not None:
                return annotation.alias
    return None


def _alias_key(
    key: str,
    type_: typing.Any,
    direction: typing.Literal["read", "write"],
    aliases_to_field_names: typing.Dict[str, str],
) -> str:
    if direction == "read":
        return aliases_to_field_names.get(key, key)
    return _get_alias_from_type(type_=type_) or key
