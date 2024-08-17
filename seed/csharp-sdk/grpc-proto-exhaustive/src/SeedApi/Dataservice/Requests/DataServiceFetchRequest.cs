using Proto = Data.V1.Grpc;

#nullable enable

namespace SeedApi;

public record DataServiceFetchRequest
{
    public IEnumerable<string> Ids { get; set; } = new List<string>();

    public string? Namespace { get; set; }

    internal Proto.DataServiceFetchRequest ToProto()
    {
        var result = new Proto.DataServiceFetchRequest();
        if (Ids.Any())
        {
            result.Ids.AddRange(Ids ?? "");
        }
        if (Namespace != null)
        {
            result.Namespace = Namespace ?? "";
        }
        return result;
    }
}
