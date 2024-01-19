/**
 * This file was auto-generated by Fern from our API Definition.
 */
package com.seed.trace.resources.submission.types;

import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.seed.trace.core.ObjectMappers;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
import java.util.UUID;

@JsonInclude(JsonInclude.Include.NON_EMPTY)
@JsonDeserialize(builder = WorkspaceRanResponse.Builder.class)
public final class WorkspaceRanResponse {
    private final UUID submissionId;

    private final WorkspaceRunDetails runDetails;

    private final Map<String, Object> additionalProperties;

    private WorkspaceRanResponse(
            UUID submissionId, WorkspaceRunDetails runDetails, Map<String, Object> additionalProperties) {
        this.submissionId = submissionId;
        this.runDetails = runDetails;
        this.additionalProperties = additionalProperties;
    }

    @JsonProperty("submissionId")
    public UUID getSubmissionId() {
        return submissionId;
    }

    @JsonProperty("runDetails")
    public WorkspaceRunDetails getRunDetails() {
        return runDetails;
    }

    @java.lang.Override
    public boolean equals(Object other) {
        if (this == other) return true;
        return other instanceof WorkspaceRanResponse && equalTo((WorkspaceRanResponse) other);
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    private boolean equalTo(WorkspaceRanResponse other) {
        return submissionId.equals(other.submissionId) && runDetails.equals(other.runDetails);
    }

    @java.lang.Override
    public int hashCode() {
        return Objects.hash(this.submissionId, this.runDetails);
    }

    @java.lang.Override
    public String toString() {
        return ObjectMappers.stringify(this);
    }

    public static SubmissionIdStage builder() {
        return new Builder();
    }

    public interface SubmissionIdStage {
        RunDetailsStage submissionId(UUID submissionId);

        Builder from(WorkspaceRanResponse other);
    }

    public interface RunDetailsStage {
        _FinalStage runDetails(WorkspaceRunDetails runDetails);
    }

    public interface _FinalStage {
        WorkspaceRanResponse build();
    }

    @JsonIgnoreProperties(ignoreUnknown = true)
    public static final class Builder implements SubmissionIdStage, RunDetailsStage, _FinalStage {
        private UUID submissionId;

        private WorkspaceRunDetails runDetails;

        @JsonAnySetter
        private Map<String, Object> additionalProperties = new HashMap<>();

        private Builder() {}

        @java.lang.Override
        public Builder from(WorkspaceRanResponse other) {
            submissionId(other.getSubmissionId());
            runDetails(other.getRunDetails());
            return this;
        }

        @java.lang.Override
        @JsonSetter("submissionId")
        public RunDetailsStage submissionId(UUID submissionId) {
            this.submissionId = submissionId;
            return this;
        }

        @java.lang.Override
        @JsonSetter("runDetails")
        public _FinalStage runDetails(WorkspaceRunDetails runDetails) {
            this.runDetails = runDetails;
            return this;
        }

        @java.lang.Override
        public WorkspaceRanResponse build() {
            return new WorkspaceRanResponse(submissionId, runDetails, additionalProperties);
        }
    }
}
