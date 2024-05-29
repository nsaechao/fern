from typing import Callable, List, Optional, Set

import fern.ir.resources as ir_types
from fern.generator_exec.resources import GeneratorConfig

from fern_python.codegen import AST, Filepath
from fern_python.declaration_referencer import AbstractDeclarationReferencer
from fern_python.pydantic_codegen.pydantic_field import PydanticField

from .pydantic_generator_context import PydanticGeneratorContext
from .type_reference_to_type_hint_converter import TypeReferenceToTypeHintConverter


class PydanticGeneratorContextImpl(PydanticGeneratorContext):
    def __init__(
        self,
        ir: ir_types.IntermediateRepresentation,
        type_declaration_referencer: AbstractDeclarationReferencer[ir_types.DeclaredTypeName],
        generator_config: GeneratorConfig,
        project_module_path: AST.ModulePath,
        allow_skipping_validation: bool,
    ):
        super().__init__(ir=ir, generator_config=generator_config, allow_skipping_validation=allow_skipping_validation)
        self._type_reference_to_type_hint_converter = TypeReferenceToTypeHintConverter(
            type_declaration_referencer=type_declaration_referencer, context=self
        )
        self._type_declaration_referencer = type_declaration_referencer
        self._project_module_path = project_module_path

        # Make a map of type_id to List[PydanticField] where the list does not contain fields that are used for multiple discriminants
        # Note this does not take into account whether type_id has that field on it.
        # Shape: {type_id: List[PydanticField]}
        self._union_discriminant_fields = {}
        # Used to see if there's multiple usages for the same field and multiple discriminants
        # Shape: {type_id: {field_name: discriminant_value}}
        self._union_discriminant_fields_by_name = {}
        for type_id, _ in self.ir.types.items():
            for _, other_td in self.ir.types.items():
                if other_td.shape.get_as_union().type == "union" and type_id in other_td.referenced_types:
                    other_td.shape.get_as_union()
                    union_types = other_td.shape.get_as_union().types
                    discriminant_field = other_td.shape.get_as_union().discriminant
                    discriminant_field_wire_value = discriminant_field.wire_value
                    for union_type in union_types:
                        union_shape = union_type.shape.get_as_union()
                        member_discriminant_value = union_type.discriminant_value.wire_value

                        if union_shape.properties_type == "samePropertiesAsObject" and union_shape.type_id == type_id:
                            if type_id in self._union_discriminant_fields_by_name and discriminant_field_wire_value in self._union_discriminant_fields_by_name[type_id]:
                                discriminant_value = self._union_discriminant_fields_by_name[type_id][discriminant_field_wire_value]
                                # If you've encountered a different discriminant value for the same field, remove it
                                if discriminant_value != member_discriminant_value:
                                    self._union_discriminant_fields[type_id] = list(filter(lambda field: field.name != discriminant_field_wire_value, self._union_discriminant_fields[type_id]))
                            else:
                                if type_id not in self._union_discriminant_fields:
                                    self._union_discriminant_fields[type_id] = []
                                if type_id not in self._union_discriminant_fields_by_name:
                                    self._union_discriminant_fields_by_name[type_id] = {}
                                
                                pydantic_field = PydanticField(
                                    name=discriminant_field.name.snake_case.safe_name,
                                    pascal_case_field_name=discriminant_field.name.pascal_case.safe_name,
                                    type_hint=AST.TypeHint.literal(AST.Expression(f'"{member_discriminant_value}"')),
                                    json_field_name=discriminant_field_wire_value,
                                    default_value=member_discriminant_value,
                                )
                                
                                self._union_discriminant_fields[type_id] = self._union_discriminant_fields[type_id].append(pydantic_field)
                                self._union_discriminant_fields_by_name[type_id][discriminant_field_wire_value] = member_discriminant_value



    def get_module_path_in_project(self, module_path: AST.ModulePath) -> AST.ModulePath:
        return self._project_module_path + module_path

    def get_type_hint_for_type_reference(
        self,
        type_reference: ir_types.TypeReference,
        must_import_after_current_declaration: Optional[Callable[[ir_types.DeclaredTypeName], bool]] = None,
        in_endpoint: Optional[bool] = False,
    ) -> AST.TypeHint:
        return self._type_reference_to_type_hint_converter.get_type_hint_for_type_reference(
            type_reference,
            must_import_after_current_declaration=must_import_after_current_declaration,
            in_endpoint=in_endpoint,
        )

    def get_class_reference_for_type_id(
        self,
        type_id: ir_types.TypeId,
        must_import_after_current_declaration: Optional[Callable[[ir_types.DeclaredTypeName], bool]] = None,
    ) -> AST.ClassReference:
        declaration = self.ir.types[type_id]
        return self._type_declaration_referencer.get_class_reference(
            name=declaration.name,
            must_import_after_current_declaration=must_import_after_current_declaration,
        )

    def does_circularly_reference_itself(self, type_id: ir_types.TypeId) -> bool:
        return self.does_type_reference_other_type(type_id, type_id)

    def do_types_reference_each_other(self, a: ir_types.TypeId, b: ir_types.TypeId) -> bool:
        return self.does_type_reference_other_type(a, b) and self.does_type_reference_other_type(b, a)

    def does_type_reference_other_type(self, type_id: ir_types.TypeId, other_type_id: ir_types.TypeId) -> bool:
        referenced_types = self.get_referenced_types(type_id)
        return other_type_id in referenced_types

    def get_referenced_types(self, type_id: ir_types.TypeId) -> Set[ir_types.TypeId]:
        declaration = self.ir.types[type_id]
        return self.get_referenced_types_of_type_declaration(declaration)

    def get_declaration_for_type_id(
        self,
        type_id: ir_types.TypeId,
    ) -> ir_types.TypeDeclaration:
        return self.ir.types[type_id]

    def get_class_name_for_type_id(self, type_id: ir_types.TypeId) -> str:
        declaration = self.get_declaration_for_type_id(type_id)
        return self._type_declaration_referencer.get_class_name(name=declaration.name)

    def get_filepath_for_type_id(self, type_id: ir_types.TypeId) -> Filepath:
        declaration = self.get_declaration_for_type_id(type_id)
        return self._type_declaration_referencer.get_filepath(name=declaration.name)

    def get_all_properties_including_extensions(self, type_name: ir_types.TypeId) -> List[ir_types.ObjectProperty]:
        declaration = self.get_declaration_for_type_id(type_name)
        shape = declaration.shape.get_as_union()
        if shape.type != "object":
            raise RuntimeError(
                f"Cannot get properties because {declaration.name.name.original_name} is not an object, it's a {shape.type}"
            )

        properties = shape.properties.copy()
        for extension in shape.extends:
            properties.extend(self.get_all_properties_including_extensions(extension.type_id))

        return properties

    def get_referenced_types_of_type_declaration(
        self, type_declaration: ir_types.TypeDeclaration
    ) -> Set[ir_types.TypeId]:
        return type_declaration.referenced_types

    def get_referenced_types_of_type_reference(self, type_reference: ir_types.TypeReference) -> Set[ir_types.TypeId]:
        return type_reference.visit(
            container=lambda container: container.visit(
                list_=lambda item_type: self.get_referenced_types_of_type_reference(item_type),
                set_=lambda item_type: self.get_referenced_types_of_type_reference(item_type),
                optional=lambda item_type: self.get_referenced_types_of_type_reference(item_type),
                map_=lambda map_type: (
                    self.get_referenced_types_of_type_reference(map_type.key_type).union(
                        self.get_referenced_types_of_type_reference(map_type.value_type)
                    )
                ),
                literal=lambda literal: set(),
            ),
            primitive=lambda primitive: set(),
            named=lambda type_name: self.get_referenced_types_of_type_declaration(
                self.get_declaration_for_type_id(type_name.type_id),
            ),
            unknown=lambda: set(),
        )

    def get_type_names_in_type_reference(self, type_reference: ir_types.TypeReference) -> Set[ir_types.TypeId]:
        return type_reference.visit(
            container=lambda container: container.visit(
                list_=lambda item_type: self.get_referenced_types_of_type_reference(item_type),
                set_=lambda item_type: self.get_referenced_types_of_type_reference(item_type),
                optional=lambda item_type: self.get_referenced_types_of_type_reference(item_type),
                map_=lambda map_type: (
                    self.get_referenced_types_of_type_reference(map_type.key_type).union(
                        self.get_referenced_types_of_type_reference(map_type.value_type)
                    )
                ),
                literal=lambda literal: set(),
            ),
            primitive=lambda primitive: set(),
            named=lambda type_name: set([type_name.type_id]),
            unknown=lambda: set(),
        )

    # Returns the defaulted discriminant fields for the object if the same field is not used
    # in multiple union discriminant fields.
    def get_union_discriminant_fields(self, type_id: ir_types.TypeId, should_reuse_union_members: bool) -> List[PydanticField]:
        if not should_reuse_union_members:
            return []

        object_properties = self.get_all_properties_including_extensions(type_id)
        object_property_names = [prop.name.name.snake_case.safe_name for prop in object_properties]
        maybe_discriminant_fields = self._union_discriminant_fields.get(type_id)

        actual_discriminant_fields = []
        if maybe_discriminant_fields is None:
            return []
        else:
            for field in maybe_discriminant_fields:
                if field.name in object_property_names:
                    actual_discriminant_fields.append(field)
        return actual_discriminant_fields