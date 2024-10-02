<?php

namespace Seed\V2\V3\Problem;

use Seed\Core\Json\SerializableType;
use Seed\Commons\Language;
use Seed\Core\Json\JsonProperty;
use Seed\Core\Types\ArrayType;

class GetBasicSolutionFileResponse extends SerializableType
{
    /**
     * @var array<value-of<Language>, FileInfoV2> $solutionFileByLanguage
     */
    #[JsonProperty('solutionFileByLanguage'), ArrayType(['string' => FileInfoV2::class])]
    public array $solutionFileByLanguage;

    /**
     * @param array{
     *   solutionFileByLanguage: array<value-of<Language>, FileInfoV2>,
     * } $values
     */
    public function __construct(
        array $values,
    ) {
        $this->solutionFileByLanguage = $values['solutionFileByLanguage'];
    }
}
