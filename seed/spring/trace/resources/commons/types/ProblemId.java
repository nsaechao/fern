/**
 * This file was auto-generated by Fern from our API Definition.
 */

package resources.commons.types;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;
import java.lang.Object;
import java.lang.String;

public final class ProblemId {
  private final String value;

  private ProblemId(String value) {
    this.value = value;
  }

  @JsonValue
  public String get() {
    return this.value;
  }

  @java.lang.Override
  public boolean equals(Object other) {
    return this == other || (other instanceof ProblemId && this.value.equals(((ProblemId) other).value));
  }

  @java.lang.Override
  public int hashCode() {
    return value.hashCode();
  }

  @java.lang.Override
  public String toString() {
    return value;
  }

  @JsonCreator(
      mode = JsonCreator.Mode.DELEGATING
  )
  public static ProblemId of(String value) {
    return new ProblemId(value);
  }

  public static ProblemId valueOf(String value) {
    return of(value);
  }
}
