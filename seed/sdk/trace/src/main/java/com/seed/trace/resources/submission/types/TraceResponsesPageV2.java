/**
 * This file was auto-generated by Fern from our API Definition.
 */
package com.seed.trace.resources.submission.types;

import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.Nulls;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.seed.trace.core.ObjectMappers;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;

@JsonInclude(JsonInclude.Include.NON_EMPTY)
@JsonDeserialize(builder = TraceResponsesPageV2.Builder.class)
public final class TraceResponsesPageV2 {
    private final Optional<Integer> offset;

    private final List<TraceResponseV2> traceResponses;

    private final Map<String, Object> additionalProperties;

    private TraceResponsesPageV2(
            Optional<Integer> offset, List<TraceResponseV2> traceResponses, Map<String, Object> additionalProperties) {
        this.offset = offset;
        this.traceResponses = traceResponses;
        this.additionalProperties = additionalProperties;
    }

    /**
     * @return If present, use this to load subseqent pages.
     * The offset is the id of the next trace response to load.
     */
    @JsonProperty("offset")
    public Optional<Integer> getOffset() {
        return offset;
    }

    @JsonProperty("traceResponses")
    public List<TraceResponseV2> getTraceResponses() {
        return traceResponses;
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) return true;
        return other instanceof TraceResponsesPageV2 && equalTo((TraceResponsesPageV2) other);
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    private boolean equalTo(TraceResponsesPageV2 other) {
        return offset.equals(other.offset) && traceResponses.equals(other.traceResponses);
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.offset, this.traceResponses);
    }

    @Override
    public String toString() {
        return ObjectMappers.stringify(this);
    }

    public static Builder builder() {
        return new Builder();
    }

    @JsonIgnoreProperties(ignoreUnknown = true)
    public static final class Builder {
        private Optional<Integer> offset = Optional.empty();

        private List<TraceResponseV2> traceResponses = new ArrayList<>();

        private Builder() {}

        public Builder from(TraceResponsesPageV2 other) {
            offset(other.getOffset());
            traceResponses(other.getTraceResponses());
            return this;
        }

        @JsonSetter(value = "offset", nulls = Nulls.SKIP)
        public Builder offset(Optional<Integer> offset) {
            this.offset = offset;
            return this;
        }

        public Builder offset(Integer offset) {
            this.offset = Optional.of(offset);
            return this;
        }

        @JsonSetter(value = "traceResponses", nulls = Nulls.SKIP)
        public Builder traceResponses(List<TraceResponseV2> traceResponses) {
            this.traceResponses.clear();
            this.traceResponses.addAll(traceResponses);
            return this;
        }

        public Builder addTraceResponses(TraceResponseV2 traceResponses) {
            this.traceResponses.add(traceResponses);
            return this;
        }

        public Builder addAllTraceResponses(List<TraceResponseV2> traceResponses) {
            this.traceResponses.addAll(traceResponses);
            return this;
        }

        public TraceResponsesPageV2 build() {
            return new TraceResponsesPageV2(offset, traceResponses, additionalProperties);
        }
    }
}
