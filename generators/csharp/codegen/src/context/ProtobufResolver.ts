import {
    ProtobufFile,
    ProtobufType,
    TypeId,
    WellKnownProtobufType
} from "@fern-fern/ir-sdk/api";
import { csharp } from "..";
import { BaseCsharpCustomConfigSchema } from "../custom-config/BaseCsharpCustomConfigSchema";
import { ResolvedWellKnownProtobufType } from "../ResolvedWellKnownProtobufType";
import { AbstractCsharpGeneratorContext } from "./AbstractCsharpGeneratorContext";
import { CsharpTypeMapper } from "./CsharpTypeMapper";

export class ProtobufResolver {
    private context: AbstractCsharpGeneratorContext<BaseCsharpCustomConfigSchema>;
    private csharpTypeMapper: CsharpTypeMapper;

    public constructor(context: AbstractCsharpGeneratorContext<BaseCsharpCustomConfigSchema>, csharpTypeMapper: CsharpTypeMapper) {
        this.context = context;
        this.csharpTypeMapper = csharpTypeMapper;
    }

    /**
     * Returns the class reference for the Protobuf type identified by the given
     * type ID (e.g. `User.V1.Grpc.User`).
     */
    public getProtobufTypeOrThrow(typeId: TypeId): csharp.Type {
        const protobufType = this.getProtobufTypeForTypeId(typeId);
        if (protobufType == null) {
            throw new Error(`The type identified by ${typeId} is not a Protobuf type`);
        }
        switch (protobufType.type) {
            case "wellKnown": {
                if (protobufType.value.type === "struct") {
                    return this.getProtobufStructTypeOrThrow();
                }
                return csharp.Type.reference(this.getWellKnownProtobufTypeClassReferenceOrThrow(protobufType.value));
            }
            case "userDefined": {
                return csharp.Type.reference(
                    this.csharpTypeMapper.convertToClassReference({
                        typeId,
                        name: protobufType.name
                    })
                );
            }
        }
    }

    public getProtoConverterClassReference(): csharp.ClassReference {
        return csharp.classReference({
            name: "ProtoConverter"
            namespace: 
        })
    }

    public getNamespaceFromProtobufFileOrThrow(protobufFile: ProtobufFile): string {
        const namespace = protobufFile.options?.csharp?.namespace;
        if (namespace == null) {
            throw new Error(
                `The 'csharp_namespace' file option must be declared in Protobuf file ${protobufFile.filepath}`
            );
        }
        return namespace;
    }

    public getProtobufStructTypeOrThrow(): csharp.Type {
        const resolvedType = this.getProtobufStructType();
        if (resolvedType == null) {
            throw new Error(
                "Well-known google.protobuf.Struct type could not be found, which is required by google.protobuf.Value."
            );
        }
        return resolvedType;
    }

    public getProtobufStructType(): csharp.Type | undefined {
        const protobufStructValueReference = this.getWellKnownProtobufTypeClassReference(WellKnownProtobufType.value());
        if (protobufStructValueReference == null) {
            return undefined;
        }
        return csharp.Type.map(
            csharp.Type.string(),
            csharp.Type.optional(csharp.Type.reference(protobufStructValueReference))
        );
    }

    public getProtobufValueTypeOrThrow(): csharp.Type {
        const resolvedType = this.getProtobufStructType();
        if (resolvedType === undefined) {
            throw new Error(
                "Well-known google.protobuf.Value type could not be found, which is required by google.protobuf.Struct."
            );
        }
        return resolvedType;
    }

    public getProtobufValueType(): csharp.Type | undefined {
        const classReference = this.getWellKnownProtobufTypeClassReference(WellKnownProtobufType.value());
        if (classReference == null) {
            return undefined;
        }
        return csharp.Type.reference(classReference);
    }

    public resolveWellKnownProtobufTypeOrThrow(
        wellKnownProtobufType: WellKnownProtobufType
    ): ResolvedWellKnownProtobufType {
        const classReference = this.resolveWellKnownProtobufType(wellKnownProtobufType);
        if (classReference == null) {
            throw new Error(`Well-known Protobuf type "${wellKnownProtobufType.type}" could not be found.`);
        }
        return classReference;
    }

    public isAnyWellKnownProtobufType(typeId: TypeId): boolean {
        return this.isProtobufStruct(typeId) || this.isProtobufValue(typeId);
    }

    public isProtobufStruct(typeId: TypeId): boolean {
        return this.isWellKnownProtobufType({
            typeId,
            wellKnownProtobufType: WellKnownProtobufType.struct()
        });
    }

    public isProtobufValue(typeId: TypeId): boolean {
        return this.isWellKnownProtobufType({
            typeId,
            wellKnownProtobufType: WellKnownProtobufType.value()
        });
    }

    private getWellKnownProtobufTypeClassReferenceOrThrow(
        wellKnownProtobufType: WellKnownProtobufType
    ): csharp.ClassReference {
        const classReference = this.getWellKnownProtobufTypeClassReference(wellKnownProtobufType);
        if (classReference == null) {
            throw new Error(`Well-known Protobuf type "${wellKnownProtobufType.type}" could not be found.`);
        }
        return classReference;
    }

    private getWellKnownProtobufTypeClassReference(
        wellKnownProtobufType: WellKnownProtobufType
    ): csharp.ClassReference | undefined {
        const resolvedType = this.resolveWellKnownProtobufType(wellKnownProtobufType);
        if (resolvedType == null) {
            return undefined;
        }
        return this.csharpTypeMapper.convertToClassReference(resolvedType.typeDeclaration.name);
    }

    private resolveWellKnownProtobufType(
        wellKnownProtobufType: WellKnownProtobufType
    ): ResolvedWellKnownProtobufType | undefined {
        for (const [typeId, typeDeclaration] of Object.entries(this.context.ir.types)) {
            if (this.isWellKnownProtobufType({ typeId, wellKnownProtobufType })) {
                return {
                    typeDeclaration,
                    wellKnownProtobufType
                };
            }
        }
        return undefined;
    }

    private isWellKnownProtobufType({
        typeId,
        wellKnownProtobufType
    }: {
        typeId: TypeId;
        wellKnownProtobufType: WellKnownProtobufType;
    }): boolean {
        const protobufType = this.getProtobufTypeForTypeId(typeId);
        if (protobufType == null) {
            return false;
        }
        return protobufType.type === "wellKnown" && protobufType.value.type === wellKnownProtobufType.type;
    }

    private getProtobufTypeForTypeId(typeId: TypeId): ProtobufType | undefined {
        const typeDeclaration = this.context.ir.types[typeId];
        if (typeDeclaration?.source == null) {
            return undefined;
        }
        return typeDeclaration.source.type === "proto" ? typeDeclaration.source.value : undefined;
    }
}
