/**
 * This file was auto-generated by Fern from our API Definition.
 */
package com.seed.api.model;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.Nulls;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.seed.api.core.ObjectMappers;
import java.util.Objects;
import java.util.Optional;

@JsonInclude(JsonInclude.Include.NON_ABSENT)
@JsonDeserialize(builder = Usage.Builder.class)
public final class Usage {
    private final Optional<Integer> units;

    private Usage(Optional<Integer> units) {
        this.units = units;
    }

    @JsonProperty("units")
    public Optional<Integer> getUnits() {
        return units;
    }

    @java.lang.Override
    public boolean equals(Object other) {
        if (this == other) return true;
        return other instanceof Usage && equalTo((Usage) other);
    }

    private boolean equalTo(Usage other) {
        return units.equals(other.units);
    }

    @java.lang.Override
    public int hashCode() {
        return Objects.hash(this.units);
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
        private Optional<Integer> units = Optional.empty();

        private Builder() {}

        public Builder from(Usage other) {
            units(other.getUnits());
            return this;
        }

        @JsonSetter(value = "units", nulls = Nulls.SKIP)
        public Builder units(Optional<Integer> units) {
            this.units = units;
            return this;
        }

        public Builder units(Integer units) {
            this.units = Optional.ofNullable(units);
            return this;
        }

        public Usage build() {
            return new Usage(units);
        }
    }
}
