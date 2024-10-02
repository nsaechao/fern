<?php

namespace Seed\V2\V3\Problem;

use Seed\Core\Json\SerializableType;
use Seed\Core\Json\JsonProperty;
use Seed\Core\Types\ArrayType;

class VoidFunctionDefinition extends SerializableType
{
    /**
     * @var array<Parameter> $parameters
     */
    #[JsonProperty('parameters'), ArrayType([Parameter::class])]
    public array $parameters;

    /**
     * @var FunctionImplementationForMultipleLanguages $code
     */
    #[JsonProperty('code')]
    public FunctionImplementationForMultipleLanguages $code;

    /**
     * @param array{
     *   parameters: array<Parameter>,
     *   code: FunctionImplementationForMultipleLanguages,
     * } $values
     */
    public function __construct(
        array $values,
    ) {
        $this->parameters = $values['parameters'];
        $this->code = $values['code'];
    }
}
