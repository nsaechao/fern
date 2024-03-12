# This file was auto-generated by Fern from our API Definition.

import os

import pytest
from seed.client import SeedPackageYml, AsyncSeedPackageYml


@pytest.fixture
def client() -> SeedPackageYml:
    return SeedPackageYml(base_url=os.getenv("TESTS_BASE_URL", "base_url")
    )
@pytest.fixture
def async_client() -> AsyncSeedPackageYml:
    return AsyncSeedPackageYml(base_url=os.getenv("TESTS_BASE_URL", "base_url")
    )
