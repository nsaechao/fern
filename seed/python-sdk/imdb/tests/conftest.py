# This file was auto-generated by Fern from our API Definition.

import os

import pytest
from seed.client import SeedApi, AsyncSeedApi


@pytest.fixture
def client() -> SeedApi:
    return SeedApi(token=os.getenv("ENV_TOKEN", "token")
    , base_url=os.getenv("TESTS_BASE_URL", "base_url")
    )
@pytest.fixture
def async_client() -> AsyncSeedApi:
    return AsyncSeedApi(token=os.getenv("ENV_TOKEN", "token")
    , base_url=os.getenv("TESTS_BASE_URL", "base_url")
    )
