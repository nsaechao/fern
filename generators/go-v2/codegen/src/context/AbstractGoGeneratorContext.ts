import { AbstractGeneratorContext, FernGeneratorExec, GeneratorNotificationService } from "@fern-api/generator-commons";
import {
    IntermediateRepresentation,
    Literal,
    Name,
    TypeReference,
    TypeId,
    TypeDeclaration,
    Subpackage,
    SubpackageId,
    FernFilepath,
    PrimitiveTypeV1
} from "@fern-fern/ir-sdk/api";
import { BaseGoCustomConfigSchema } from "../custom-config/BaseGoCustomConfigSchema";
import { GoTypeMapper } from "./GoTypeMapper";
import { RelativeFilePath } from "@fern-api/fs-utils";
import { go } from "..";
import { TimeTypeReference, UuidTypeReference } from "../ast/Type";

const DEFAULT_MODULE_PATH = "sdk";

export interface FileLocation {
    importPath: string;
    directory: RelativeFilePath;
}

export abstract class AbstractGoGeneratorContext<
    CustomConfig extends BaseGoCustomConfigSchema
> extends AbstractGeneratorContext {
    private rootImportPath: string;
    public readonly goTypeMapper: GoTypeMapper;

    public constructor(
        public readonly ir: IntermediateRepresentation,
        public readonly config: FernGeneratorExec.config.GeneratorConfig,
        public readonly customConfig: CustomConfig,
        public readonly generatorNotificationService: GeneratorNotificationService
    ) {
        super(config, generatorNotificationService);
        this.goTypeMapper = new GoTypeMapper(this);
        this.rootImportPath = this.resolveRootImportPath({
            customConfig: this.customConfig
        });
    }

    public getSubpackageOrThrow(subpackageId: SubpackageId): Subpackage {
        const subpackage = this.ir.subpackages[subpackageId];
        if (subpackage == null) {
            throw new Error(`Subpackage with id ${subpackageId} not found`);
        }
        return subpackage;
    }

    public getClassName(name: Name): string {
        return name.pascalCase.safeName;
    }

    public getRootImportPath(): string {
        return this.rootImportPath;
    }

    public getCoreImportPath(): string {
        return `${this.rootImportPath}/core`;
    }

    public getFieldName(name: Name): string {
        return name.pascalCase.unsafeName;
    }

    public getLiteralAsString(literal: Literal): string {
        return literal.type === "string" ? `'${literal.string}'` : literal.boolean ? "'true'" : "'false'";
    }

    public getUuidTypeReference(): go.TypeReference {
        return UuidTypeReference;
    }

    public getTimeTypeReference(): go.TypeReference {
        return TimeTypeReference;
    }

    public isOptional(typeReference: TypeReference): boolean {
        switch (typeReference.type) {
            case "container":
                return typeReference.container.type === "optional";
            case "named": {
                const typeDeclaration = this.getTypeDeclarationOrThrow(typeReference.typeId);
                if (typeDeclaration.shape.type === "alias") {
                    return this.isOptional(typeDeclaration.shape.aliasOf);
                }
                return false;
            }
            case "unknown":
                return false;
            case "primitive":
                return false;
        }
    }

    public isEnum(typeReference: TypeReference): boolean {
        switch (typeReference.type) {
            case "container":
                if (typeReference.container.type === "optional") {
                    return this.isEnum(typeReference.container.optional);
                }
                return false;
            case "named": {
                const declaration = this.getTypeDeclarationOrThrow(typeReference.typeId);
                return this.typeDeclarationIsEnum(declaration);
            }
            case "primitive": {
                return false;
            }
            case "unknown": {
                return false;
            }
        }
    }

    public typeDeclarationIsEnum(declaration: TypeDeclaration): boolean {
        if (declaration.shape.type === "alias") {
            return this.isEnum(declaration.shape.aliasOf);
        }
        return declaration.shape.type === "enum";
    }

    public isDate(typeReference: TypeReference): boolean {
        return this.isPrimitive({ typeReference, primitive: PrimitiveTypeV1.Date });
    }

    public isDateTime(typeReference: TypeReference): boolean {
        return this.isPrimitive({ typeReference, primitive: PrimitiveTypeV1.DateTime });
    }

    public isPrimitive({
        typeReference,
        primitive
    }: {
        typeReference: TypeReference;
        primitive?: PrimitiveTypeV1;
    }): boolean {
        switch (typeReference.type) {
            case "container":
                if (typeReference.container.type === "optional") {
                    return this.isDate(typeReference.container.optional);
                }
                return false;
            case "named": {
                const declaration = this.getTypeDeclarationOrThrow(typeReference.typeId);
                if (declaration.shape.type === "alias") {
                    return this.isDate(declaration.shape.aliasOf);
                }
                return false;
            }
            case "primitive": {
                if (primitive == null) {
                    return true;
                }
                return typeReference.primitive.v1 === primitive;
            }
            case "unknown": {
                return false;
            }
        }
    }

    public maybeLiteral(typeReference: TypeReference): Literal | undefined {
        if (typeReference.type === "container" && typeReference.container.type === "literal") {
            return typeReference.container.literal;
        }
        return undefined;
    }

    public getTypeDeclarationOrThrow(typeId: TypeId): TypeDeclaration {
        const typeDeclaration = this.getTypeDeclaration(typeId);
        if (typeDeclaration == null) {
            throw new Error(`Type declaration with id ${typeId} not found`);
        }
        return typeDeclaration;
    }

    public getTypeDeclaration(typeId: TypeId): TypeDeclaration | undefined {
        return this.ir.types[typeId];
    }

    public abstract getLocationForTypeId(typeId: TypeId): FileLocation;

    protected getFileLocation(filepath: FernFilepath, suffix?: string): FileLocation {
        let parts = filepath.packagePath.map((path) => path.pascalCase.safeName.toLowerCase());
        parts = suffix != null ? [...parts, suffix] : parts;
        return {
            importPath: [this.getRootImportPath(), ...parts].join("/"),
            directory: RelativeFilePath.of(parts.join("/"))
        };
    }

    private resolveRootImportPath({ customConfig }: { customConfig: BaseGoCustomConfigSchema }): string {
        const suffix = this.getMajorVersionSuffix();
        if (customConfig.importPath != null) {
            return customConfig.importPath + suffix;
        }
        if (customConfig.module != null) {
            return customConfig.module.path + suffix;
        }
        return DEFAULT_MODULE_PATH + suffix;
    }

    private getMajorVersionSuffix(): string | undefined {
        const majorVersion = this.parseMajorVersion();
        if (majorVersion == null) {
            return undefined;
        }
        return `/v${majorVersion}`;
    }

    private parseMajorVersion(): string | undefined {
        if (this.version == null) {
            return undefined;
        }
        const split = this.version.split(".");
        if (split[0] == null) {
            return undefined;
        }
        return split[0];
    }
}
