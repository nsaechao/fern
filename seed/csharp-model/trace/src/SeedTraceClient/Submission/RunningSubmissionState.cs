using System.Text.Json.Serialization;
using System;
using SeedTraceClient.Utilities;

namespace SeedTraceClient;

[JsonConverter(typeof(TolerantEnumConverter))]
public enum RunningSubmissionState
{
    [EnumMember(Value = "QUEUEING_SUBMISSION")]
    QueueingSubmission,

    [EnumMember(Value = "KILLING_HISTORICAL_SUBMISSIONS")]
    KillingHistoricalSubmissions,

    [EnumMember(Value = "WRITING_SUBMISSION_TO_FILE")]
    WritingSubmissionToFile,

    [EnumMember(Value = "COMPILING_SUBMISSION")]
    CompilingSubmission,

    [EnumMember(Value = "RUNNING_SUBMISSION")]
    RunningSubmission
}
