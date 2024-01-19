/**
 * This file was auto-generated by Fern from our API Definition.
 */
package com.seed.literal.resources.literal.requests;

import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.Nulls;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.seed.literal.core.ObjectMappers;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Objects;

@JsonInclude(JsonInclude.Include.NON_EMPTY)
@JsonDeserialize(builder = CreateOptionsRequest.Builder.class)
public final class CreateOptionsRequest {
    private final Map<String, String> values;

    private final Map<String, Object> additionalProperties;

    private CreateOptionsRequest(Map<String, String> values, Map<String, Object> additionalProperties) {
        this.values = values;
        this.additionalProperties = additionalProperties;
    }

    @JsonProperty("values")
    public Map<String, String> getValues() {
        return values;
    }

    @java.lang.Override
    public boolean equals(Object other) {
        if (this == other) return true;
        return other instanceof CreateOptionsRequest && equalTo((CreateOptionsRequest) other);
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    private boolean equalTo(CreateOptionsRequest other) {
        return values.equals(other.values);
    }

    @java.lang.Override
    public int hashCode() {
        return Objects.hash(this.values);
    }

    @java.lang.Override
    public String toString() {
        return ObjectMappers.stringify(this);
    }

    public static Builder builder() {
        return new Builder();
    }

    @JsonIgnoreProperties(ignoreUnknown = true)
    public static final class Builder {
        private Map<String, String> values = new LinkedHashMap<>();

        @JsonAnySetter
        private Map<String, Object> additionalProperties = new HashMap<>();

        private Builder() {}

        public Builder from(CreateOptionsRequest other) {
            values(other.getValues());
            return this;
        }

        @JsonSetter(value = "values", nulls = Nulls.SKIP)
        public Builder values(Map<String, String> values) {
            this.values.clear();
            this.values.putAll(values);
            return this;
        }

        public Builder putAllValues(Map<String, String> values) {
            this.values.putAll(values);
            return this;
        }

        public Builder values(String key, String value) {
            this.values.put(key, value);
            return this;
        }

        public CreateOptionsRequest build() {
            return new CreateOptionsRequest(values, additionalProperties);
        }
    }
}
