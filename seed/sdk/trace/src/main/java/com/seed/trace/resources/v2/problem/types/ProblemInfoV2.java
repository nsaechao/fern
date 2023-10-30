/**
 * This file was auto-generated by Fern from our API Definition.
 */
package com.seed.trace.resources.v2.problem.types;

import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.Nulls;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.seed.trace.core.ObjectMappers;
import com.seed.trace.resources.commons.types.Language;
import com.seed.trace.resources.problem.types.ProblemDescription;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;

@JsonInclude(JsonInclude.Include.NON_EMPTY)
@JsonDeserialize(builder = ProblemInfoV2.Builder.class)
public final class ProblemInfoV2 {
    private final String problemId;

    private final ProblemDescription problemDescription;

    private final String problemName;

    private final int problemVersion;

    private final Set<Language> supportedLanguages;

    private final CustomFiles customFiles;

    private final GeneratedFiles generatedFiles;

    private final List<TestCaseTemplate> customTestCaseTemplates;

    private final List<TestCaseV2> testcases;

    private final boolean isPublic;

    private final Map<String, Object> additionalProperties;

    private ProblemInfoV2(
            String problemId,
            ProblemDescription problemDescription,
            String problemName,
            int problemVersion,
            Set<Language> supportedLanguages,
            CustomFiles customFiles,
            GeneratedFiles generatedFiles,
            List<TestCaseTemplate> customTestCaseTemplates,
            List<TestCaseV2> testcases,
            boolean isPublic,
            Map<String, Object> additionalProperties) {
        this.problemId = problemId;
        this.problemDescription = problemDescription;
        this.problemName = problemName;
        this.problemVersion = problemVersion;
        this.supportedLanguages = supportedLanguages;
        this.customFiles = customFiles;
        this.generatedFiles = generatedFiles;
        this.customTestCaseTemplates = customTestCaseTemplates;
        this.testcases = testcases;
        this.isPublic = isPublic;
        this.additionalProperties = additionalProperties;
    }

    @JsonProperty("problemId")
    public String getProblemId() {
        return problemId;
    }

    @JsonProperty("problemDescription")
    public ProblemDescription getProblemDescription() {
        return problemDescription;
    }

    @JsonProperty("problemName")
    public String getProblemName() {
        return problemName;
    }

    @JsonProperty("problemVersion")
    public int getProblemVersion() {
        return problemVersion;
    }

    @JsonProperty("supportedLanguages")
    public Set<Language> getSupportedLanguages() {
        return supportedLanguages;
    }

    @JsonProperty("customFiles")
    public CustomFiles getCustomFiles() {
        return customFiles;
    }

    @JsonProperty("generatedFiles")
    public GeneratedFiles getGeneratedFiles() {
        return generatedFiles;
    }

    @JsonProperty("customTestCaseTemplates")
    public List<TestCaseTemplate> getCustomTestCaseTemplates() {
        return customTestCaseTemplates;
    }

    @JsonProperty("testcases")
    public List<TestCaseV2> getTestcases() {
        return testcases;
    }

    @JsonProperty("isPublic")
    public boolean getIsPublic() {
        return isPublic;
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) return true;
        return other instanceof ProblemInfoV2 && equalTo((ProblemInfoV2) other);
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    private boolean equalTo(ProblemInfoV2 other) {
        return problemId.equals(other.problemId)
                && problemDescription.equals(other.problemDescription)
                && problemName.equals(other.problemName)
                && problemVersion == other.problemVersion
                && supportedLanguages.equals(other.supportedLanguages)
                && customFiles.equals(other.customFiles)
                && generatedFiles.equals(other.generatedFiles)
                && customTestCaseTemplates.equals(other.customTestCaseTemplates)
                && testcases.equals(other.testcases)
                && isPublic == other.isPublic;
    }

    @Override
    public int hashCode() {
        return Objects.hash(
                this.problemId,
                this.problemDescription,
                this.problemName,
                this.problemVersion,
                this.supportedLanguages,
                this.customFiles,
                this.generatedFiles,
                this.customTestCaseTemplates,
                this.testcases,
                this.isPublic);
    }

    @Override
    public String toString() {
        return ObjectMappers.stringify(this);
    }

    public static ProblemIdStage builder() {
        return new Builder();
    }

    public interface ProblemIdStage {
        ProblemDescriptionStage problemId(String problemId);

        Builder from(ProblemInfoV2 other);
    }

    public interface ProblemDescriptionStage {
        ProblemNameStage problemDescription(ProblemDescription problemDescription);
    }

    public interface ProblemNameStage {
        ProblemVersionStage problemName(String problemName);
    }

    public interface ProblemVersionStage {
        CustomFilesStage problemVersion(int problemVersion);
    }

    public interface CustomFilesStage {
        GeneratedFilesStage customFiles(CustomFiles customFiles);
    }

    public interface GeneratedFilesStage {
        IsPublicStage generatedFiles(GeneratedFiles generatedFiles);
    }

    public interface IsPublicStage {
        _FinalStage isPublic(boolean isPublic);
    }

    public interface _FinalStage {
        ProblemInfoV2 build();

        _FinalStage supportedLanguages(Set<Language> supportedLanguages);

        _FinalStage addSupportedLanguages(Language supportedLanguages);

        _FinalStage addAllSupportedLanguages(Set<Language> supportedLanguages);

        _FinalStage customTestCaseTemplates(List<TestCaseTemplate> customTestCaseTemplates);

        _FinalStage addCustomTestCaseTemplates(TestCaseTemplate customTestCaseTemplates);

        _FinalStage addAllCustomTestCaseTemplates(List<TestCaseTemplate> customTestCaseTemplates);

        _FinalStage testcases(List<TestCaseV2> testcases);

        _FinalStage addTestcases(TestCaseV2 testcases);

        _FinalStage addAllTestcases(List<TestCaseV2> testcases);
    }

    @JsonIgnoreProperties(ignoreUnknown = true)
    public static final class Builder
            implements ProblemIdStage,
                    ProblemDescriptionStage,
                    ProblemNameStage,
                    ProblemVersionStage,
                    CustomFilesStage,
                    GeneratedFilesStage,
                    IsPublicStage,
                    _FinalStage {
        private String problemId;

        private ProblemDescription problemDescription;

        private String problemName;

        private int problemVersion;

        private CustomFiles customFiles;

        private GeneratedFiles generatedFiles;

        private boolean isPublic;

        private List<TestCaseV2> testcases = new ArrayList<>();

        private List<TestCaseTemplate> customTestCaseTemplates = new ArrayList<>();

        private Set<Language> supportedLanguages = new LinkedHashSet<>();

        @JsonAnySetter
        private Map<String, Object> additionalProperties = new HashMap<>();

        private Builder() {}

        @Override
        public Builder from(ProblemInfoV2 other) {
            problemId(other.getProblemId());
            problemDescription(other.getProblemDescription());
            problemName(other.getProblemName());
            problemVersion(other.getProblemVersion());
            supportedLanguages(other.getSupportedLanguages());
            customFiles(other.getCustomFiles());
            generatedFiles(other.getGeneratedFiles());
            customTestCaseTemplates(other.getCustomTestCaseTemplates());
            testcases(other.getTestcases());
            isPublic(other.getIsPublic());
            return this;
        }

        @Override
        @JsonSetter("problemId")
        public ProblemDescriptionStage problemId(String problemId) {
            this.problemId = problemId;
            return this;
        }

        @Override
        @JsonSetter("problemDescription")
        public ProblemNameStage problemDescription(ProblemDescription problemDescription) {
            this.problemDescription = problemDescription;
            return this;
        }

        @Override
        @JsonSetter("problemName")
        public ProblemVersionStage problemName(String problemName) {
            this.problemName = problemName;
            return this;
        }

        @Override
        @JsonSetter("problemVersion")
        public CustomFilesStage problemVersion(int problemVersion) {
            this.problemVersion = problemVersion;
            return this;
        }

        @Override
        @JsonSetter("customFiles")
        public GeneratedFilesStage customFiles(CustomFiles customFiles) {
            this.customFiles = customFiles;
            return this;
        }

        @Override
        @JsonSetter("generatedFiles")
        public IsPublicStage generatedFiles(GeneratedFiles generatedFiles) {
            this.generatedFiles = generatedFiles;
            return this;
        }

        @Override
        @JsonSetter("isPublic")
        public _FinalStage isPublic(boolean isPublic) {
            this.isPublic = isPublic;
            return this;
        }

        @Override
        public _FinalStage addAllTestcases(List<TestCaseV2> testcases) {
            this.testcases.addAll(testcases);
            return this;
        }

        @Override
        public _FinalStage addTestcases(TestCaseV2 testcases) {
            this.testcases.add(testcases);
            return this;
        }

        @Override
        @JsonSetter(value = "testcases", nulls = Nulls.SKIP)
        public _FinalStage testcases(List<TestCaseV2> testcases) {
            this.testcases.clear();
            this.testcases.addAll(testcases);
            return this;
        }

        @Override
        public _FinalStage addAllCustomTestCaseTemplates(List<TestCaseTemplate> customTestCaseTemplates) {
            this.customTestCaseTemplates.addAll(customTestCaseTemplates);
            return this;
        }

        @Override
        public _FinalStage addCustomTestCaseTemplates(TestCaseTemplate customTestCaseTemplates) {
            this.customTestCaseTemplates.add(customTestCaseTemplates);
            return this;
        }

        @Override
        @JsonSetter(value = "customTestCaseTemplates", nulls = Nulls.SKIP)
        public _FinalStage customTestCaseTemplates(List<TestCaseTemplate> customTestCaseTemplates) {
            this.customTestCaseTemplates.clear();
            this.customTestCaseTemplates.addAll(customTestCaseTemplates);
            return this;
        }

        @Override
        public _FinalStage addAllSupportedLanguages(Set<Language> supportedLanguages) {
            this.supportedLanguages.addAll(supportedLanguages);
            return this;
        }

        @Override
        public _FinalStage addSupportedLanguages(Language supportedLanguages) {
            this.supportedLanguages.add(supportedLanguages);
            return this;
        }

        @Override
        @JsonSetter(value = "supportedLanguages", nulls = Nulls.SKIP)
        public _FinalStage supportedLanguages(Set<Language> supportedLanguages) {
            this.supportedLanguages.clear();
            this.supportedLanguages.addAll(supportedLanguages);
            return this;
        }

        @Override
        public ProblemInfoV2 build() {
            return new ProblemInfoV2(
                    problemId,
                    problemDescription,
                    problemName,
                    problemVersion,
                    supportedLanguages,
                    customFiles,
                    generatedFiles,
                    customTestCaseTemplates,
                    testcases,
                    isPublic,
                    additionalProperties);
        }
    }
}
