<?php

namespace Seed\V2\V3\Problem\Types;

use Seed\Core\SerializableType;
use Seed\Commons\Types\Language;
use Seed\Core\JsonProperty;
use Seed\Core\ArrayType;

class GetFunctionSignatureResponse extends SerializableType
{
    /**
     * @var array<Language, string> $functionByLanguage
     */
    #[JsonProperty('functionByLanguage'), ArrayType([Language::class => 'string'])]
    public array $functionByLanguage;

    /**
     * @param array{
     *   functionByLanguage: array<Language, string>,
     * } $values
     */
    public function __construct(
        array $values,
    ) {
        $this->functionByLanguage = $values['functionByLanguage'];
    }
}
