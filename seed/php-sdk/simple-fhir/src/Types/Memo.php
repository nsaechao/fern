<?php

namespace Seed\Types;

use Seed\Core\Json\SerializableType;
use Seed\Core\Json\JsonProperty;

class Memo extends SerializableType
{
    /**
     * @var string $description
     */
    #[JsonProperty('description')]
    public string $description;

    /**
     * @var ?Account $account
     */
    #[JsonProperty('account')]
    public ?Account $account;

    /**
     * @param array{
     *   description: string,
     *   account?: ?Account,
     * } $values
     */
    public function __construct(
        array $values,
    ) {
        $this->description = $values['description'];
        $this->account = $values['account'] ?? null;
    }
}
