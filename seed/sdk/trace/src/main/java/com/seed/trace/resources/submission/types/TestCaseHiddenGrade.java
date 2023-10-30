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

@JsonInclude(JsonInclude.Include.NON_EMPTY)
@JsonDeserialize(builder = TestCaseHiddenGrade.Builder.class)
public final class TestCaseHiddenGrade {
    private final boolean passed;

    private final Map<String, Object> additionalProperties;

    private TestCaseHiddenGrade(boolean passed, Map<String, Object> additionalProperties) {
        this.passed = passed;
        this.additionalProperties = additionalProperties;
    }

    @JsonProperty("passed")
    public boolean getPassed() {
        return passed;
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) return true;
        return other instanceof TestCaseHiddenGrade && equalTo((TestCaseHiddenGrade) other);
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    private boolean equalTo(TestCaseHiddenGrade other) {
        return passed == other.passed;
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.passed);
    }

    @Override
    public String toString() {
        return ObjectMappers.stringify(this);
    }

    public static PassedStage builder() {
        return new Builder();
    }

    public interface PassedStage {
        _FinalStage passed(boolean passed);

        Builder from(TestCaseHiddenGrade other);
    }

    public interface _FinalStage {
        TestCaseHiddenGrade build();
    }

    @JsonIgnoreProperties(ignoreUnknown = true)
    public static final class Builder implements PassedStage, _FinalStage {
        private boolean passed;

        @JsonAnySetter
        private Map<String, Object> additionalProperties = new HashMap<>();

        private Builder() {}

        @Override
        public Builder from(TestCaseHiddenGrade other) {
            passed(other.getPassed());
            return this;
        }

        @Override
        @JsonSetter("passed")
        public _FinalStage passed(boolean passed) {
            this.passed = passed;
            return this;
        }

        @Override
        public TestCaseHiddenGrade build() {
            return new TestCaseHiddenGrade(passed, additionalProperties);
        }
    }
}
