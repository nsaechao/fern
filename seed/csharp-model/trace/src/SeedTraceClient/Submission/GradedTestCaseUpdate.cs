using System.Text.Json.Serialization;
using OneOf;
using SeedTraceClient;

namespace SeedTraceClient;

public class GradedTestCaseUpdate
{
    [JsonPropertyName("testCaseId")]
    public string TestCaseId { get; init; }

    [JsonPropertyName("grade")]
    public OneOf<TestCaseGrade._Hidden, TestCaseGrade._NonHidden> Grade { get; init; }
}
