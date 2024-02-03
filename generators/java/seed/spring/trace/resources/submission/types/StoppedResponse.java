/**
 * This file was auto-generated by Fern from our API Definition.
 */

package resources.submission.types;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import core.ObjectMappers;
import java.lang.Object;
import java.lang.String;
import java.util.Objects;

@JsonInclude(JsonInclude.Include.NON_EMPTY)
@JsonDeserialize(
    builder = StoppedResponse.Builder.class
)
public final class StoppedResponse {
  private final SubmissionId submissionId;

  private StoppedResponse(SubmissionId submissionId) {
    this.submissionId = submissionId;
  }

  @JsonProperty("submissionId")
  public SubmissionId getSubmissionId() {
    return submissionId;
  }

  @java.lang.Override
  public boolean equals(Object other) {
    if (this == other) return true;
    return other instanceof StoppedResponse && equalTo((StoppedResponse) other);
  }

  private boolean equalTo(StoppedResponse other) {
    return submissionId.equals(other.submissionId);
  }

  @java.lang.Override
  public int hashCode() {
    return Objects.hash(this.submissionId);
  }

  @java.lang.Override
  public String toString() {
    return ObjectMappers.stringify(this);
  }

  public static SubmissionIdStage builder() {
    return new Builder();
  }

  public interface SubmissionIdStage {
    _FinalStage submissionId(SubmissionId submissionId);

    Builder from(StoppedResponse other);
  }

  public interface _FinalStage {
    StoppedResponse build();
  }

  @JsonIgnoreProperties(
      ignoreUnknown = true
  )
  public static final class Builder implements SubmissionIdStage, _FinalStage {
    private SubmissionId submissionId;

    private Builder() {
    }

    @java.lang.Override
    public Builder from(StoppedResponse other) {
      submissionId(other.getSubmissionId());
      return this;
    }

    @java.lang.Override
    @JsonSetter("submissionId")
    public _FinalStage submissionId(SubmissionId submissionId) {
      this.submissionId = submissionId;
      return this;
    }

    @java.lang.Override
    public StoppedResponse build() {
      return new StoppedResponse(submissionId);
    }
  }
}
