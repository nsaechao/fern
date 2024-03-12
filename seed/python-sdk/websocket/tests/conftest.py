# This file was auto-generated by Fern from our API Definition.

import os

import pytest
from seed.client import SeedWebsocket, AsyncSeedWebsocket


@pytest.fixture
def client() -> SeedWebsocket:
    return SeedWebsocket(base_url=os.getenv("TESTS_BASE_URL", "base_url")
    )
@pytest.fixture
def async_client() -> AsyncSeedWebsocket:
    return AsyncSeedWebsocket(base_url=os.getenv("TESTS_BASE_URL", "base_url")
    )
