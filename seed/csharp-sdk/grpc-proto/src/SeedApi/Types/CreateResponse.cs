using System.Text.Json.Serialization;

#nullable enable

namespace SeedApi;

public record CreateResponse
{
    [JsonPropertyName("user")]
    public UserModel? User { get; set; }

    internal User.V1.CreateResponse ToProto()
    {
        var result = new User.V1.CreateResponse();
        if (User != null)
        {
            result.User = User.ToProto();
        }
        return result;
    }
}
