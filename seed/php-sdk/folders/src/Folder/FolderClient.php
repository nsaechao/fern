<?php

namespace Seed\Folder;

use Seed\Folder\Service\ServiceClient;
use Seed\Core\RawClient;
use Seed\Core\JsonApiRequest;
use Seed\Core\HttpMethod;
use Psr\Http\Client\ClientExceptionInterface;
use Exception;

class FolderClient
{
    /**
     * @var ServiceClient $service
     */
    public ServiceClient $service;

    /**
     * @var RawClient $client
     */
    private RawClient $client;

    /**
     * @param RawClient $client
     */
    public function __construct(
        RawClient $client,
    ) {
        $this->client = $client;
        $this->service = new ServiceClient($this->client);
    }

    /**
     * @param ?array{baseUrl?: string} $options
     */
    public function foo(?array $options = null): void
    {
        try {
            $response = $this->client->sendRequest(
                new JsonApiRequest(
                    baseUrl: $this->options['baseUrl'] ?? $this->client->options['baseUrl'] ?? '',
                    path: "",
                    method: HttpMethod::POST,
                ),
            );
            $statusCode = $response->getStatusCode();
            if ($statusCode >= 200 && $statusCode < 400) {
                return;
            }
        } catch (ClientExceptionInterface $e) {
            throw new Exception($e->getMessage());
        }
        throw new Exception("Error with status code " . $statusCode);
    }

}
