<?php

namespace Seed\Commons\Types;

use Seed\Core\Json\SerializableType;
use Seed\Core\Json\JsonProperty;

class MapType extends SerializableType
{
    /**
     * @var mixed $keyType
     */
    #[JsonProperty('keyType')]
    public mixed $keyType;

    /**
     * @var mixed $valueType
     */
    #[JsonProperty('valueType')]
    public mixed $valueType;

    /**
     * @param array{
     *   keyType: mixed,
     *   valueType: mixed,
     * } $values
     */
    public function __construct(
        array $values,
    ) {
        $this->keyType = $values['keyType'];
        $this->valueType = $values['valueType'];
    }
}
