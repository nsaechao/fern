using System.Text.Json.Serialization;

#nullable enable

namespace SeedTrace;

public record BuildingExecutorResponse
{
    [JsonPropertyName("submissionId")]
    public required string SubmissionId { get; set; }

    [JsonPropertyName("status")]
    public required ExecutionSessionStatus Status { get; set; }
}
