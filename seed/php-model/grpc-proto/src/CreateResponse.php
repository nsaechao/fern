<?php

namespace Seed;

use Seed\Core\Json\SerializableType;
use Seed\Core\Json\JsonProperty;

class CreateResponse extends SerializableType
{
    /**
     * @var ?UserModel $user
     */
    #[JsonProperty('user')]
    public ?UserModel $user;

    /**
     * @param array{
     *   user?: ?UserModel,
     * } $values
     */
    public function __construct(
        array $values = [],
    ) {
        $this->user = $values['user'] ?? null;
    }
}
