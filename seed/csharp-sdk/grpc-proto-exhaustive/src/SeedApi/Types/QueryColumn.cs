using System.Text.Json.Serialization;
using Proto = Data.V1.Grpc;

#nullable enable

namespace SeedApi;

public record QueryColumn
{
    [JsonPropertyName("values")]
    public IEnumerable<float> Values { get; set; } = new List<float>();

    [JsonPropertyName("topK")]
    public uint? TopK { get; set; }

    [JsonPropertyName("namespace")]
    public string? Namespace { get; set; }

    [JsonPropertyName("filter")]
    public object? Filter { get; set; }

    [JsonPropertyName("indexedData")]
    public IndexedData? IndexedData { get; set; }

    internal Proto.QueryColumn ToProto()
    {
        var result = new Proto.QueryColumn();
        if (Values.Any())
        {
            result.Values.AddRange(Values);
        }
        if (TopK != null)
        {
            result.TopK = TopK ?? 0U;
        }
        if (Namespace != null)
        {
            result.Namespace = Namespace ?? "";
        }
        if (Filter != null && Filter.Any())
        {
            foreach (var kvp in Filter)
            {
                result.Filter.Add(kvp.Key, kvp.Value);
            }
            ;
        }
        if (IndexedData != null)
        {
            result.IndexedData = IndexedData.ToProto();
        }
        return result;
    }
}
