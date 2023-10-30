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
import com.seed.trace.resources.commons.types.Language;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

@JsonInclude(JsonInclude.Include.NON_EMPTY)
@JsonDeserialize(builder = UnexpectedLanguageError.Builder.class)
public final class UnexpectedLanguageError {
    private final Language expectedLanguage;

    private final Language actualLanguage;

    private final Map<String, Object> additionalProperties;

    private UnexpectedLanguageError(
            Language expectedLanguage, Language actualLanguage, Map<String, Object> additionalProperties) {
        this.expectedLanguage = expectedLanguage;
        this.actualLanguage = actualLanguage;
        this.additionalProperties = additionalProperties;
    }

    @JsonProperty("expectedLanguage")
    public Language getExpectedLanguage() {
        return expectedLanguage;
    }

    @JsonProperty("actualLanguage")
    public Language getActualLanguage() {
        return actualLanguage;
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) return true;
        return other instanceof UnexpectedLanguageError && equalTo((UnexpectedLanguageError) other);
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    private boolean equalTo(UnexpectedLanguageError other) {
        return expectedLanguage.equals(other.expectedLanguage) && actualLanguage.equals(other.actualLanguage);
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.expectedLanguage, this.actualLanguage);
    }

    @Override
    public String toString() {
        return ObjectMappers.stringify(this);
    }

    public static ExpectedLanguageStage builder() {
        return new Builder();
    }

    public interface ExpectedLanguageStage {
        ActualLanguageStage expectedLanguage(Language expectedLanguage);

        Builder from(UnexpectedLanguageError other);
    }

    public interface ActualLanguageStage {
        _FinalStage actualLanguage(Language actualLanguage);
    }

    public interface _FinalStage {
        UnexpectedLanguageError build();
    }

    @JsonIgnoreProperties(ignoreUnknown = true)
    public static final class Builder implements ExpectedLanguageStage, ActualLanguageStage, _FinalStage {
        private Language expectedLanguage;

        private Language actualLanguage;

        @JsonAnySetter
        private Map<String, Object> additionalProperties = new HashMap<>();

        private Builder() {}

        @Override
        public Builder from(UnexpectedLanguageError other) {
            expectedLanguage(other.getExpectedLanguage());
            actualLanguage(other.getActualLanguage());
            return this;
        }

        @Override
        @JsonSetter("expectedLanguage")
        public ActualLanguageStage expectedLanguage(Language expectedLanguage) {
            this.expectedLanguage = expectedLanguage;
            return this;
        }

        @Override
        @JsonSetter("actualLanguage")
        public _FinalStage actualLanguage(Language actualLanguage) {
            this.actualLanguage = actualLanguage;
            return this;
        }

        @Override
        public UnexpectedLanguageError build() {
            return new UnexpectedLanguageError(expectedLanguage, actualLanguage, additionalProperties);
        }
    }
}
