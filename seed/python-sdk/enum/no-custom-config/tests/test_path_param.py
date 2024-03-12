# This file was auto-generated by Fern from our API Definition.

from seed import Color, Operand
from seed.client import SeedEnum, AsyncSeedEnum


async def test_send(client: SeedEnum, async_client: AsyncSeedEnum) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.path_param.send(operand=Operand.GREATER_THAN, maybe_operand=Operand.LESS_THAN, operand_or_color=Color.RED, maybe_operand_or_color=Color.RED) is None  # type: ignore[func-returns-value]
    
    assert await async_client.path_param.send(operand=Operand.GREATER_THAN, maybe_operand=Operand.LESS_THAN, operand_or_color=Color.RED, maybe_operand_or_color=Color.RED) is None  # type: ignore[func-returns-value]
