# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from .dog import Dog as resources_types_resources_union_types_dog_Dog
from .cat import Cat as resources_types_resources_union_types_cat_Cat
from ......core.pydantic_utilities import UniversalRootModel
import typing
from ......core.pydantic_utilities import IS_PYDANTIC_V2
import typing_extensions
import pydantic
T_Result = typing.TypeVar("T_Result")
class _Factory:
    
    def dog(self, value: resources_types_resources_union_types_dog_Dog) -> Animal:
        return Animal(_Animal.Dog(**value.dict(exclude_unset=True), animal="dog"))
    
    def cat(self, value: resources_types_resources_union_types_cat_Cat) -> Animal:
        return Animal(_Animal.Cat(**value.dict(exclude_unset=True), animal="cat"))
class Animal(UniversalRootModel):
    factory: typing.ClassVar[_Factory] = _Factory()
    
    if IS_PYDANTIC_V2:
        root: typing_extensions.Annotated[typing.Union[_Animal.Dog, _Animal.Cat], pydantic.Field(discriminator="animal")]
        def get_as_union(self) -> typing.Union[_Animal.Dog, _Animal.Cat]:
            return self.root
    else:
        __root__: typing_extensions.Annotated[typing.Union[_Animal.Dog, _Animal.Cat], pydantic.Field(discriminator="animal")]
        def get_as_union(self) -> typing.Union[_Animal.Dog, _Animal.Cat]:
            return self.__root__
    
    def visit(self, dog: typing.Callable[[resources_types_resources_union_types_dog_Dog], T_Result], cat: typing.Callable[[resources_types_resources_union_types_cat_Cat], T_Result]) -> T_Result:
        if self.get_as_union().animal == "dog":
            return dog(
            resources_types_resources_union_types_dog_Dog(**self.get_as_union().dict(exclude_unset=True, exclude={"animal"})))
        if self.get_as_union().animal == "cat":
            return cat(
            resources_types_resources_union_types_cat_Cat(**self.get_as_union().dict(exclude_unset=True, exclude={"animal"})))
class _Animal:
    
    class Dog(resources_types_resources_union_types_dog_Dog):
        animal: typing.Literal["dog"] = "dog"
        
        class Config:
            allow_population_by_field_name = True
    
    class Cat(resources_types_resources_union_types_cat_Cat):
        animal: typing.Literal["cat"] = "cat"
        
        class Config:
            allow_population_by_field_name = True
