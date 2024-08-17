using Proto = Data.V1.Grpc;

#nullable enable

namespace SeedApi;

public record DataServiceListRequest
{
    public string? Prefix { get; set; }

    public uint? Limit { get; set; }

    public string? PaginationToken { get; set; }

    public string? Namespace { get; set; }

    internal Proto.DataServiceListRequest ToProto()
    {
        var result = new Proto.DataServiceListRequest();
        if (Prefix != null)
        {
            result.Prefix = Prefix ?? "";
        }
        if (Limit != null)
        {
            result.Limit = Limit ?? 0U;
        }
        if (PaginationToken != null)
        {
            result.PaginationToken = PaginationToken ?? "";
        }
        if (Namespace != null)
        {
            result.Namespace = Namespace ?? "";
        }
        return result;
    }
}
