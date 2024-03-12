# This file was auto-generated by Fern from our API Definition.

import os

import pytest
from seed.client import SeedObjectsWithImports, AsyncSeedObjectsWithImports


@pytest.fixture
def client() -> SeedObjectsWithImports:
    return SeedObjectsWithImports(base_url=os.getenv("TESTS_BASE_URL", "base_url")
    )
@pytest.fixture
def async_client() -> AsyncSeedObjectsWithImports:
    return AsyncSeedObjectsWithImports(base_url=os.getenv("TESTS_BASE_URL", "base_url")
    )
