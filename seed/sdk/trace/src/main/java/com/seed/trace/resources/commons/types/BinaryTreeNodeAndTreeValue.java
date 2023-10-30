/**
 * This file was auto-generated by Fern from our API Definition.
 */
package com.seed.trace.resources.commons.types;

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
@JsonDeserialize(builder = BinaryTreeNodeAndTreeValue.Builder.class)
public final class BinaryTreeNodeAndTreeValue {
    private final String nodeId;

    private final BinaryTreeValue fullTree;

    private final Map<String, Object> additionalProperties;

    private BinaryTreeNodeAndTreeValue(
            String nodeId, BinaryTreeValue fullTree, Map<String, Object> additionalProperties) {
        this.nodeId = nodeId;
        this.fullTree = fullTree;
        this.additionalProperties = additionalProperties;
    }

    @JsonProperty("nodeId")
    public String getNodeId() {
        return nodeId;
    }

    @JsonProperty("fullTree")
    public BinaryTreeValue getFullTree() {
        return fullTree;
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) return true;
        return other instanceof BinaryTreeNodeAndTreeValue && equalTo((BinaryTreeNodeAndTreeValue) other);
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    private boolean equalTo(BinaryTreeNodeAndTreeValue other) {
        return nodeId.equals(other.nodeId) && fullTree.equals(other.fullTree);
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.nodeId, this.fullTree);
    }

    @Override
    public String toString() {
        return ObjectMappers.stringify(this);
    }

    public static NodeIdStage builder() {
        return new Builder();
    }

    public interface NodeIdStage {
        FullTreeStage nodeId(String nodeId);

        Builder from(BinaryTreeNodeAndTreeValue other);
    }

    public interface FullTreeStage {
        _FinalStage fullTree(BinaryTreeValue fullTree);
    }

    public interface _FinalStage {
        BinaryTreeNodeAndTreeValue build();
    }

    @JsonIgnoreProperties(ignoreUnknown = true)
    public static final class Builder implements NodeIdStage, FullTreeStage, _FinalStage {
        private String nodeId;

        private BinaryTreeValue fullTree;

        @JsonAnySetter
        private Map<String, Object> additionalProperties = new HashMap<>();

        private Builder() {}

        @Override
        public Builder from(BinaryTreeNodeAndTreeValue other) {
            nodeId(other.getNodeId());
            fullTree(other.getFullTree());
            return this;
        }

        @Override
        @JsonSetter("nodeId")
        public FullTreeStage nodeId(String nodeId) {
            this.nodeId = nodeId;
            return this;
        }

        @Override
        @JsonSetter("fullTree")
        public _FinalStage fullTree(BinaryTreeValue fullTree) {
            this.fullTree = fullTree;
            return this;
        }

        @Override
        public BinaryTreeNodeAndTreeValue build() {
            return new BinaryTreeNodeAndTreeValue(nodeId, fullTree, additionalProperties);
        }
    }
}
