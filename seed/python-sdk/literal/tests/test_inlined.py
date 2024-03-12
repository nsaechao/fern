# This file was auto-generated by Fern from our API Definition.

from seed.client import SeedLiteral, AsyncSeedLiteral

from .utilities import validate_response


async def test_send(client: SeedLiteral, async_client: AsyncSeedLiteral) -> None:
    expected_response = {'message': 'The weather is sunny', 'status': 200, 'success': True}
    response = client.inlined.send(temperature=10.1, query="What is the weather today")
    validate_response(response, expected_response)
    
    async_response = await async_client.inlined.send(temperature=10.1, query="What is the weather today")
    validate_response(async_response, expected_response)
