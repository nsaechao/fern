import fern.ir.resources as ir_types
from fern.generator_exec.resources import GeneratorConfig

from fern_python.codegen import AST, Filepath

from ..declaration_referencers import (
    ErrorDeclarationReferencer,
    InlinedRequestDeclarationReferencer,
    ServiceDeclarationReferencer,
    ServiceNameAndInlinedRequestBody,
)
from .fastapi_generator_context import FastApiGeneratorContext


class FastApiGeneratorContextImpl(FastApiGeneratorContext):
    def __init__(
        self,
        ir: ir_types.IntermediateRepresentation,
        generator_config: GeneratorConfig,
        project_module_path: AST.ModulePath,
    ):
        super().__init__(ir=ir, generator_config=generator_config, project_module_path=project_module_path)
        self._service_declaration_referencer = ServiceDeclarationReferencer()
        self._error_declaration_referencer = ErrorDeclarationReferencer()
        self._inlined_request_declaration_referencer = InlinedRequestDeclarationReferencer(
            service_declaration_handler=self._service_declaration_referencer,
        )

    def get_filepath_for_service(self, service_name: ir_types.DeclaredServiceName) -> Filepath:
        return self._service_declaration_referencer.get_filepath(name=service_name)

    def get_class_name_for_service(self, service_name: ir_types.DeclaredServiceName) -> str:
        return self._service_declaration_referencer.get_class_name(name=service_name)

    def get_reference_to_service(self, service_name: ir_types.DeclaredServiceName) -> AST.ClassReference:
        return self._service_declaration_referencer.get_class_reference(name=service_name, as_request=False)

    def get_filepath_for_inlined_request(
        self, service_name: ir_types.DeclaredServiceName, request: ir_types.InlinedRequestBody
    ) -> Filepath:
        return self._inlined_request_declaration_referencer.get_filepath(
            name=ServiceNameAndInlinedRequestBody(service_name=service_name, request=request)
        )

    def get_class_name_for_inlined_request(
        self, service_name: ir_types.DeclaredServiceName, request: ir_types.InlinedRequestBody
    ) -> str:
        return self._inlined_request_declaration_referencer.get_class_name(
            name=ServiceNameAndInlinedRequestBody(service_name=service_name, request=request)
        )

    def get_reference_to_inlined_request(
        self, service_name: ir_types.DeclaredServiceName, request: ir_types.InlinedRequestBody
    ) -> AST.ClassReference:
        return self._inlined_request_declaration_referencer.get_class_reference(
            name=ServiceNameAndInlinedRequestBody(service_name=service_name, request=request),
            as_request=False
        )

    def get_filepath_for_error(self, error_name: ir_types.DeclaredErrorName) -> Filepath:
        return self._error_declaration_referencer.get_filepath(name=error_name)

    def get_class_name_for_error(self, error_name: ir_types.DeclaredErrorName) -> str:
        return self._error_declaration_referencer.get_class_name(name=error_name)

    def get_reference_to_error(self, error_name: ir_types.DeclaredErrorName) -> AST.ClassReference:
        return self._error_declaration_referencer.get_class_reference(name=error_name, as_request=False)
