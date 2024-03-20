using System.Text.Json.Serialization;
using OneOf;
using SeedTraceClient.V2;

namespace SeedTraceClient.V2;

public class TestCaseImplementationDescription
{
    [JsonPropertyName("boards")]
    public List<OneOf<TestCaseImplementationDescriptionBoard._Html, TestCaseImplementationDescriptionBoard._ParamId>> Boards { get; init; }
}
