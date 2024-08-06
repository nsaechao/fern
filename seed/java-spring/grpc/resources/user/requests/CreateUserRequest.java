/**
 * This file was auto-generated by Fern from our API Definition.
 */

package resources.user.requests;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.Nulls;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import core.ObjectMappers;
import java.lang.Double;
import java.lang.Integer;
import java.lang.Object;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;

@JsonInclude(JsonInclude.Include.NON_ABSENT)
@JsonDeserialize(
    builder = CreateUserRequest.Builder.class
)
public final class CreateUserRequest {
  private final String username;

  private final Optional<String> email;

  private final Optional<Integer> age;

  private final Optional<Double> weight;

  private CreateUserRequest(String username, Optional<String> email, Optional<Integer> age,
      Optional<Double> weight) {
    this.username = username;
    this.email = email;
    this.age = age;
    this.weight = weight;
  }

  @JsonProperty("username")
  public String getUsername() {
    return username;
  }

  @JsonProperty("email")
  public Optional<String> getEmail() {
    return email;
  }

  @JsonProperty("age")
  public Optional<Integer> getAge() {
    return age;
  }

  @JsonProperty("weight")
  public Optional<Double> getWeight() {
    return weight;
  }

  @java.lang.Override
  public boolean equals(Object other) {
    if (this == other) return true;
    return other instanceof CreateUserRequest && equalTo((CreateUserRequest) other);
  }

  private boolean equalTo(CreateUserRequest other) {
    return username.equals(other.username) && email.equals(other.email) && age.equals(other.age) && weight.equals(other.weight);
  }

  @java.lang.Override
  public int hashCode() {
    return Objects.hash(this.username, this.email, this.age, this.weight);
  }

  @java.lang.Override
  public String toString() {
    return ObjectMappers.stringify(this);
  }

  public static UsernameStage builder() {
    return new Builder();
  }

  public interface UsernameStage {
    _FinalStage username(String username);

    Builder from(CreateUserRequest other);
  }

  public interface _FinalStage {
    CreateUserRequest build();

    _FinalStage email(Optional<String> email);

    _FinalStage email(String email);

    _FinalStage age(Optional<Integer> age);

    _FinalStage age(Integer age);

    _FinalStage weight(Optional<Double> weight);

    _FinalStage weight(Double weight);
  }

  @JsonIgnoreProperties(
      ignoreUnknown = true
  )
  public static final class Builder implements UsernameStage, _FinalStage {
    private String username;

    private Optional<Double> weight = Optional.empty();

    private Optional<Integer> age = Optional.empty();

    private Optional<String> email = Optional.empty();

    private Builder() {
    }

    @java.lang.Override
    public Builder from(CreateUserRequest other) {
      username(other.getUsername());
      email(other.getEmail());
      age(other.getAge());
      weight(other.getWeight());
      return this;
    }

    @java.lang.Override
    @JsonSetter("username")
    public _FinalStage username(String username) {
      this.username = username;
      return this;
    }

    @java.lang.Override
    public _FinalStage weight(Double weight) {
      this.weight = Optional.ofNullable(weight);
      return this;
    }

    @java.lang.Override
    @JsonSetter(
        value = "weight",
        nulls = Nulls.SKIP
    )
    public _FinalStage weight(Optional<Double> weight) {
      this.weight = weight;
      return this;
    }

    @java.lang.Override
    public _FinalStage age(Integer age) {
      this.age = Optional.ofNullable(age);
      return this;
    }

    @java.lang.Override
    @JsonSetter(
        value = "age",
        nulls = Nulls.SKIP
    )
    public _FinalStage age(Optional<Integer> age) {
      this.age = age;
      return this;
    }

    @java.lang.Override
    public _FinalStage email(String email) {
      this.email = Optional.ofNullable(email);
      return this;
    }

    @java.lang.Override
    @JsonSetter(
        value = "email",
        nulls = Nulls.SKIP
    )
    public _FinalStage email(Optional<String> email) {
      this.email = email;
      return this;
    }

    @java.lang.Override
    public CreateUserRequest build() {
      return new CreateUserRequest(username, email, age, weight);
    }
  }
}
