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
    builder = ExceptionInfo.Builder.class
)
public final class ExceptionInfo {
  private final String exceptionType;

  private final String exceptionMessage;

  private final String exceptionStacktrace;

  private ExceptionInfo(String exceptionType, String exceptionMessage, String exceptionStacktrace) {
    this.exceptionType = exceptionType;
    this.exceptionMessage = exceptionMessage;
    this.exceptionStacktrace = exceptionStacktrace;
  }

  @JsonProperty("exceptionType")
  public String getExceptionType() {
    return exceptionType;
  }

  @JsonProperty("exceptionMessage")
  public String getExceptionMessage() {
    return exceptionMessage;
  }

  @JsonProperty("exceptionStacktrace")
  public String getExceptionStacktrace() {
    return exceptionStacktrace;
  }

  @java.lang.Override
  public boolean equals(Object other) {
    if (this == other) return true;
    return other instanceof ExceptionInfo && equalTo((ExceptionInfo) other);
  }

  private boolean equalTo(ExceptionInfo other) {
    return exceptionType.equals(other.exceptionType) && exceptionMessage.equals(other.exceptionMessage) && exceptionStacktrace.equals(other.exceptionStacktrace);
  }

  @java.lang.Override
  public int hashCode() {
    return Objects.hash(this.exceptionType, this.exceptionMessage, this.exceptionStacktrace);
  }

  @java.lang.Override
  public String toString() {
    return ObjectMappers.stringify(this);
  }

  public static ExceptionTypeStage builder() {
    return new Builder();
  }

  public interface ExceptionTypeStage {
    ExceptionMessageStage exceptionType(String exceptionType);

    Builder from(ExceptionInfo other);
  }

  public interface ExceptionMessageStage {
    ExceptionStacktraceStage exceptionMessage(String exceptionMessage);
  }

  public interface ExceptionStacktraceStage {
    _FinalStage exceptionStacktrace(String exceptionStacktrace);
  }

  public interface _FinalStage {
    ExceptionInfo build();
  }

  @JsonIgnoreProperties(
      ignoreUnknown = true
  )
  public static final class Builder implements ExceptionTypeStage, ExceptionMessageStage, ExceptionStacktraceStage, _FinalStage {
    private String exceptionType;

    private String exceptionMessage;

    private String exceptionStacktrace;

    private Builder() {
    }

    @java.lang.Override
    public Builder from(ExceptionInfo other) {
      exceptionType(other.getExceptionType());
      exceptionMessage(other.getExceptionMessage());
      exceptionStacktrace(other.getExceptionStacktrace());
      return this;
    }

    @java.lang.Override
    @JsonSetter("exceptionType")
    public ExceptionMessageStage exceptionType(String exceptionType) {
      this.exceptionType = exceptionType;
      return this;
    }

    @java.lang.Override
    @JsonSetter("exceptionMessage")
    public ExceptionStacktraceStage exceptionMessage(String exceptionMessage) {
      this.exceptionMessage = exceptionMessage;
      return this;
    }

    @java.lang.Override
    @JsonSetter("exceptionStacktrace")
    public _FinalStage exceptionStacktrace(String exceptionStacktrace) {
      this.exceptionStacktrace = exceptionStacktrace;
      return this;
    }

    @java.lang.Override
    public ExceptionInfo build() {
      return new ExceptionInfo(exceptionType, exceptionMessage, exceptionStacktrace);
    }
  }
}
