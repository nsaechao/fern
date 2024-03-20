using SeedTraceClient;
using System.Text.Json.Serialization;

namespace SeedTraceClient;

public class CreateProblemError
{
    public class _Generic : GenericCreateProblemError
    {
        [JsonPropertyName("_type")]
        public string ErrorType { get; } = "generic";
    }
}
