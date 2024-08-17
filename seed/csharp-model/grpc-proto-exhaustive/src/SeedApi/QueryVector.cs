using System.Text.Json.Serialization;
using SeedApi.Core;
using Proto = Data.V1.Grpc;

#nullable enable

namespace SeedApi;

public record QueryVector
{
    [JsonPropertyName("filter")]
    public Dictionary<string, MetadataValue?>? Filter { get; set; }

    internal Proto.QueryVector ToProto()
    {
        var result = new Proto.QueryVector();
        if (Filter != null)
        {
            result.Filter = ProtoConverter.ToProtoStruct(Filter);
        }
        return result;
    }
}
