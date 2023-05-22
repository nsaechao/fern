package generator

import (
	"bytes"
	"fmt"
	"go/format"
	"go/parser"
	"go/token"
	"strconv"
	"strings"

	"github.com/fern-api/fern-go/internal/types"
	"golang.org/x/tools/go/ast/astutil"
)

// fileWriter wries and formats Go files.
type fileWriter struct {
	filename    string
	packageName string
	imports     imports
	buffer      *bytes.Buffer

	// TODO: Do we need some sort of type registry so that we can consult other types
	// based on their DeclaredTypeName? This will let us handle 'extends', for example.
}

func newFileWriter(filename string) *fileWriter {
	// The default set of imports used in the generated output.
	// These imports are removed from the generated output if
	// they aren't used.
	imports := make(imports)
	imports.Add("time")
	imports.Add("github.com/gofrs/uuid")

	return &fileWriter{
		filename: filename,
		buffer:   new(bytes.Buffer),
		imports:  imports,
	}
}

// P writes the given element into a single line, concluding with a newline.
func (f *fileWriter) P(elements ...any) {
	for _, element := range elements {
		fmt.Fprint(f.buffer, element)
	}
	fmt.Fprintln(f.buffer)
}

// Finish formats and writes the content stored in the writer's buffer into a *File.
func (f *fileWriter) File() (*File, error) {
	// Start with the package declaration and import statements.
	header := newFileWriter(f.filename)
	header.P("package ", f.packageName)
	header.P("import (")
	for importDecl, importAlias := range f.imports {
		header.P(fmt.Sprintf("%s %q", importAlias, importDecl))
	}
	header.P(")")

	formatted, err := removeUnusedImports(f.filename, append(header.buffer.Bytes(), f.buffer.Bytes()...))
	if err != nil {
		return nil, err
	}
	return &File{
		Path:    f.filename,
		Content: formatted,
	}, nil
}

// AddPackage adds the package declaration to be written later.
func (f *fileWriter) AddPackage(apiName *types.Name) error {
	f.packageName = strings.ToLower(apiName.CamelCase.SafeName)
	return nil
}

// WriteType writes a complete type, including all of its properties.
func (f *fileWriter) WriteType(typeDeclaration *types.TypeDeclaration) error {
	visitor := &typeVisitor{
		typeName: typeDeclaration.Name.Name.PascalCase.UnsafeName,
		writer:   f,
	}
	return typeDeclaration.Shape.Accept(visitor)
}

// typeReferenceToGoType maps the given type reference into its Go-equivalent.
// TODO: Handle the case where this type is defined in another package.
func typeReferenceToGoType(typeReference *types.TypeReference) string {
	visitor := new(typeReferenceVisitor)
	_ = typeReference.Accept(visitor)
	return visitor.value
}

// containerTypeToGoType maps the given container type into its Go-equivalent.
func containerTypeToGoType(containerType *types.ContainerType) string {
	visitor := new(containerTypeVisitor)
	_ = containerType.Accept(visitor)
	return visitor.value
}

// literalToGoType maps the given literal into its Go-equivalent.
func literalToGoType(literal *types.Literal) string {
	visitor := new(literalVisitor)
	_ = literal.Accept(visitor)
	return visitor.value
}

// typeVisitor writes the internal properties of types (e.g. properties).
type typeVisitor struct {
	typeName string
	writer   *fileWriter
}

// Compile-time assertion.
var _ types.TypeVisitor = (*typeVisitor)(nil)

func (t *typeVisitor) VisitAlias(alias *types.AliasTypeDeclaration) error {
	t.writer.P("type ", t.typeName, " = ", typeReferenceToGoType(alias.AliasOf))
	t.writer.P()
	return nil
}

func (t *typeVisitor) VisitObject(object *types.ObjectTypeDeclaration) error {
	// TODO: Write extended properties.
	t.writer.P("type ", t.typeName, " struct {")
	for _, property := range object.Properties {
		t.writer.P(property.Name.Name.PascalCase.UnsafeName, " ", typeReferenceToGoType(property.ValueType), " `json:\"", property.Name.Name.CamelCase.UnsafeName, "\"`")
	}
	t.writer.P("}")
	t.writer.P()
	return nil
}

// typeReferenceVisitor retrieves the string representation of type references
// (e.g. containers, primitives, etc).
type typeReferenceVisitor struct {
	value string
}

// Compile-time assertion.
var _ types.TypeReferenceVisitor = (*typeReferenceVisitor)(nil)

func (t *typeReferenceVisitor) VisitContainer(container *types.ContainerType) error {
	t.value = containerTypeToGoType(container)
	return nil
}

func (t *typeReferenceVisitor) VisitNamed(named *types.DeclaredTypeName) error {
	// TODO: Need to determine whether or not the type is an enum, custom type, etc.
	// We only want to prefix with a pointer if it's a custom type (not an enum).
	t.value = fmt.Sprintf("*%s", named.Name.PascalCase.UnsafeName)
	return nil
}

func (t *typeReferenceVisitor) VisitPrimitive(primitive types.PrimitiveType) error {
	t.value = primitiveToGoType(primitive)
	return nil
}

func (t *typeReferenceVisitor) VisitUnknown(unknown any) error {
	t.value = unknownToGoType(unknown)
	return nil
}

// containerTypeVisitor retrieves the string representation of container types
// (e.g. lists, maps, etc).
type containerTypeVisitor struct {
	value string
}

// Compile-time assertion.
var _ types.ContainerTypeVisitor = (*containerTypeVisitor)(nil)

func (c *containerTypeVisitor) VisitList(list *types.TypeReference) error {
	c.value = fmt.Sprintf("[]%s", typeReferenceToGoType(list))
	return nil
}

func (c *containerTypeVisitor) VisitMap(mapType *types.MapType) error {
	c.value = fmt.Sprintf("map[%s]%s", typeReferenceToGoType(mapType.KeyType), typeReferenceToGoType(mapType.ValueType))
	return nil
}

func (c *containerTypeVisitor) VisitOptional(optional *types.TypeReference) error {
	c.value = fmt.Sprintf("*%s", typeReferenceToGoType(optional))
	return nil
}

func (c *containerTypeVisitor) VisitSet(set *types.TypeReference) error {
	c.value = fmt.Sprintf("[]%s", typeReferenceToGoType(set))
	return nil
}

func (c *containerTypeVisitor) VisitLiteral(literal *types.Literal) error {
	c.value = literalToGoType(literal)
	return nil
}

// containerTypeVisitor retrieves the string representation of literal types.
// Strings are the only supported literals for now.
type literalVisitor struct {
	value string
}

// Compile-time assertion.
var _ types.LiteralVisitor = (*literalVisitor)(nil)

func (l *literalVisitor) VisitString(value string) error {
	l.value = value
	return nil
}

// unknownToGoType maps the given unknown into its Go-equivalent.
func unknownToGoType(_ any) string {
	return "any"
}

// primitiveToGoType maps Fern's primitive types to their Go-equivalent.
func primitiveToGoType(primitive types.PrimitiveType) string {
	switch primitive {
	case types.PrimitiveTypeInteger:
		return "int"
	case types.PrimitiveTypeDouble:
		return "float64"
	case types.PrimitiveTypeString:
		return "string"
	case types.PrimitiveTypeBoolean:
		return "bool"
	case types.PrimitiveTypeLong:
		return "int64"
	// TODO: We'll need to add some special handling for [un]marshaling Date[Time] to and from time.Time.
	case types.PrimitiveTypeDateTime:
		return "time.Time"
	case types.PrimitiveTypeDate:
		return "time.Time"
	case types.PrimitiveTypeUUID:
		return "uuid.UUID"
	case types.PrimitiveTypeBase64:
		return "[]byte"
	default:
		return "any"
	}
}

// removeUnusedImports parses the buffer, interpreting it as Go code,
// and removes all unused imports. If successful, the result is then
// formatted.
func removeUnusedImports(filename string, buf []byte) ([]byte, error) {
	fset := token.NewFileSet()
	f, err := parser.ParseFile(fset, filename, buf, parser.ParseComments)
	if err != nil {
		return nil, fmt.Errorf("failed to parse Go code: %v", err)
	}

	imports := make(map[string]string)
	for _, route := range f.Imports {
		importPath, err := strconv.Unquote(route.Path.Value)
		if err != nil {
			// Unreachable. If the file parsed successfully,
			// the unquote will never fail.
			return nil, err
		}
		imports[route.Name.Name] = importPath
	}

	for name, path := range imports {
		if !astutil.UsesImport(f, path) {
			astutil.DeleteNamedImport(fset, f, name, path)
		}
	}

	var buffer bytes.Buffer
	if err := format.Node(&buffer, fset, f); err != nil {
		return nil, fmt.Errorf("failed to format Go code: %v", err)
	}

	return buffer.Bytes(), nil
}
