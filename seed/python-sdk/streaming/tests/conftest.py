# This file was auto-generated by Fern from our API Definition.

import os

import pytest
from seed.client import SeedStreaming, AsyncSeedStreaming


@pytest.fixture
def client() -> SeedStreaming:
    return SeedStreaming(base_url=os.getenv("TESTS_BASE_URL", "base_url")
    )
@pytest.fixture
def async_client() -> AsyncSeedStreaming:
    return AsyncSeedStreaming(base_url=os.getenv("TESTS_BASE_URL", "base_url")
    )
