<?php

namespace Seed\Tests\Core\Json;

use PHPUnit\Framework\TestCase;
use Seed\Core\Json\JsonProperty;
use Seed\Core\Json\SerializableType;
use Seed\Core\Types\ArrayType;
use Seed\Core\Types\Union;

class UnionArrayType extends SerializableType
{
    /**
     * @var array<int, string|int|null> $mixedArray
     */
    #[ArrayType(['integer' => new Union('string', 'integer', 'null')])]
    #[JsonProperty('mixed_array')]
    public array $mixedArray;

    /**
     * @param array{
     *   mixedArray: array<int, string|int|null>,
     * } $values
     */
    public function __construct(
        array $values,
    ) {
        $this->mixedArray = $values['mixedArray'];
    }
}

class UnionArrayTypeTest extends TestCase
{
    public function testUnionTypesInArrays(): void
    {
        $data = [
            'mixed_array' => [
                1 => 'one',
                2 => 2,
                3 => null
            ]
        ];

        $json = json_encode($data, JSON_THROW_ON_ERROR);

        $object = UnionArrayType::fromJson($json);

        $this->assertEquals('one', $object->mixedArray[1], 'mixed_array[1] should be "one".');
        $this->assertEquals(2, $object->mixedArray[2], 'mixed_array[2] should be 2.');
        $this->assertNull($object->mixedArray[3], 'mixed_array[3] should be null.');

        $serializedJson = $object->toJson();

        $this->assertJsonStringEqualsJsonString($json, $serializedJson, 'Serialized JSON does not match original JSON for mixed_array.');
    }
}
