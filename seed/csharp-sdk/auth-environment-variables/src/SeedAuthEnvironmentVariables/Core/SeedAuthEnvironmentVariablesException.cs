using System;

#nullable enable

namespace SeedAuthEnvironmentVariables.Core;

/// <summary>
/// Base exception class for all exceptions thrown by the SDK.
/// </summary>
public class SeedAuthEnvironmentVariablesException(string message, Exception? innerException = null)
    : Exception(message, innerException) { }
