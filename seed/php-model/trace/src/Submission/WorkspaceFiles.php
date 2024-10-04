<?php

namespace Seed\Submission;

use Seed\Core\Json\JsonSerializableType;
use Seed\Commons\FileInfo;
use Seed\Core\Json\JsonProperty;
use Seed\Core\Types\ArrayType;

class WorkspaceFiles extends JsonSerializableType
{
    /**
     * @var FileInfo $mainFile
     */
    #[JsonProperty('mainFile')]
    public FileInfo $mainFile;

    /**
     * @var array<FileInfo> $readOnlyFiles
     */
    #[JsonProperty('readOnlyFiles'), ArrayType([FileInfo::class])]
    public array $readOnlyFiles;

    /**
     * @param array{
     *   mainFile: FileInfo,
     *   readOnlyFiles: array<FileInfo>,
     * } $values
     */
    public function __construct(
        array $values,
    ) {
        $this->mainFile = $values['mainFile'];
        $this->readOnlyFiles = $values['readOnlyFiles'];
    }
}
