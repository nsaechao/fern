<?php

namespace Seed\Foo\Types;

use Seed\Core\Json\SerializableType;
use Seed\Core\Json\JsonProperty;

class ImportingType extends SerializableType
{
    /**
     * @var string $imported
     */
    #[JsonProperty('imported')]
    public string $imported;

    /**
     * @param array{
     *   imported: string,
     * } $values
     */
    public function __construct(
        array $values,
    ) {
        $this->imported = $values['imported'];
    }
}
