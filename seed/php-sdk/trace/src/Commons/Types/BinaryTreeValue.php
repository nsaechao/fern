<?php

namespace Seed\Commons\Types;

use Seed\Core\Json\JsonSerializableType;
use Seed\Core\Json\JsonProperty;
use Seed\Core\Types\ArrayType;

class BinaryTreeValue extends JsonSerializableType
{
    /**
     * @var ?string $root
     */
    #[JsonProperty('root')]
    public ?string $root;

    /**
     * @var array<string, BinaryTreeNodeValue> $nodes
     */
    #[JsonProperty('nodes'), ArrayType(['string' => BinaryTreeNodeValue::class])]
    public array $nodes;

    /**
     * @param array{
     *   root?: ?string,
     *   nodes: array<string, BinaryTreeNodeValue>,
     * } $values
     */
    public function __construct(
        array $values,
    ) {
        $this->root = $values['root'] ?? null;
        $this->nodes = $values['nodes'];
    }
}
