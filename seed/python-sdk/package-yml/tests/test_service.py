# This file was auto-generated by Fern from our API Definition.

from seed.client import SeedPackageYml, AsyncSeedPackageYml


async def test_nop(client: SeedPackageYml, async_client: AsyncSeedPackageYml) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.service.nop(id="id-a2ijs82", nested_id="id-219xca8") is None  # type: ignore[func-returns-value]
    
    assert await async_client.service.nop(id="id-a2ijs82", nested_id="id-219xca8") is None  # type: ignore[func-returns-value]
