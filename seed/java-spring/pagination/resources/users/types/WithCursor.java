/**
 * This file was auto-generated by Fern from our API Definition.
 */

package resources.users.types;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.Nulls;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import core.ObjectMappers;
import java.lang.Object;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;

@JsonInclude(JsonInclude.Include.NON_ABSENT)
@JsonDeserialize(
    builder = WithCursor.Builder.class
)
public final class WithCursor {
  private final Optional<String> cursor;

  private WithCursor(Optional<String> cursor) {
    this.cursor = cursor;
  }

  @JsonProperty("cursor")
  public Optional<String> getCursor() {
    return cursor;
  }

  @java.lang.Override
  public boolean equals(Object other) {
    if (this == other) return true;
    return other instanceof WithCursor && equalTo((WithCursor) other);
  }

  private boolean equalTo(WithCursor other) {
    return cursor.equals(other.cursor);
  }

  @java.lang.Override
  public int hashCode() {
    return Objects.hash(this.cursor);
  }

  @java.lang.Override
  public String toString() {
    return ObjectMappers.stringify(this);
  }

  public static Builder builder() {
    return new Builder();
  }

  @JsonIgnoreProperties(
      ignoreUnknown = true
  )
  public static final class Builder {
    private Optional<String> cursor = Optional.empty();

    private Builder() {
    }

    public Builder from(WithCursor other) {
      cursor(other.getCursor());
      return this;
    }

    @JsonSetter(
        value = "cursor",
        nulls = Nulls.SKIP
    )
    public Builder cursor(Optional<String> cursor) {
      this.cursor = cursor;
      return this;
    }

    public Builder cursor(String cursor) {
      this.cursor = Optional.of(cursor);
      return this;
    }

    public WithCursor build() {
      return new WithCursor(cursor);
    }
  }
}
