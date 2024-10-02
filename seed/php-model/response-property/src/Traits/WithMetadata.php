<?php

namespace Seed\Traits;

use Seed\Core\Json\JsonProperty;
use Seed\Core\Types\ArrayType;

trait WithMetadata
{
    /**
     * @var array<string, string> $metadata
     */
    #[JsonProperty('metadata'), ArrayType(['string' => 'string'])]
    public array $metadata;
}
