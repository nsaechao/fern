using SeedExhaustive.Core;

#nullable enable

namespace SeedExhaustive.Types;

/// <summary>
/// This exception type will be thrown for any non-2XX API responses.
/// </summary>
public class ErrorWithUnionBody(object body)
    : SeedExhaustiveApiException("ErrorWithUnionBody", 400, body)
{
    /// <summary>
    /// The body of the response that triggered the exception.
    /// </summary>
    public new object Body { get; } = body;
}
