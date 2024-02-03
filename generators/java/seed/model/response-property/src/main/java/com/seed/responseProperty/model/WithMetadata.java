/**
 * This file was auto-generated by Fern from our API Definition.
 */
package com.seed.responseProperty.model;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.Nulls;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.seed.responseProperty.core.ObjectMappers;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Objects;

@JsonInclude(JsonInclude.Include.NON_EMPTY)
@JsonDeserialize(builder = WithMetadata.Builder.class)
public final class WithMetadata implements IWithMetadata {
    private final Map<String, String> metadata;

    private WithMetadata(Map<String, String> metadata) {
        this.metadata = metadata;
    }

    @JsonProperty("metadata")
    @java.lang.Override
    public Map<String, String> getMetadata() {
        return metadata;
    }

    @java.lang.Override
    public boolean equals(Object other) {
        if (this == other) return true;
        return other instanceof WithMetadata && equalTo((WithMetadata) other);
    }

    private boolean equalTo(WithMetadata other) {
        return metadata.equals(other.metadata);
    }

    @java.lang.Override
    public int hashCode() {
        return Objects.hash(this.metadata);
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
        private Map<String, String> metadata = new LinkedHashMap<>();

        private Builder() {}

        public Builder from(WithMetadata other) {
            metadata(other.getMetadata());
            return this;
        }

        @JsonSetter(value = "metadata", nulls = Nulls.SKIP)
        public Builder metadata(Map<String, String> metadata) {
            this.metadata.clear();
            this.metadata.putAll(metadata);
            return this;
        }

        public Builder putAllMetadata(Map<String, String> metadata) {
            this.metadata.putAll(metadata);
            return this;
        }

        public Builder metadata(String key, String value) {
            this.metadata.put(key, value);
            return this;
        }

        public WithMetadata build() {
            return new WithMetadata(metadata);
        }
    }
}
