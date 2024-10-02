<?php

namespace Seed;

use Seed\Core\Json\SerializableType;
use Seed\A\A;
use Seed\Core\Json\JsonProperty;

class ImportingA extends SerializableType
{
    /**
     * @var ?A $a
     */
    #[JsonProperty('a')]
    public ?A $a;

    /**
     * @param array{
     *   a?: ?A,
     * } $values
     */
    public function __construct(
        array $values = [],
    ) {
        $this->a = $values['a'] ?? null;
    }
}
