import pytest
from sel_dedicated.configuration import Configuration
from sel_dedicated_client.api_client import ApiClient

import sel_dedicated_client


@pytest.fixture(scope='module')
def config():
    cfg = Configuration()
    cfg.api_key['X-Token'] = "{paste your access token here}"
    return cfg


@pytest.fixture(scope='module')
def client(config):
    client = ApiClient(config)
    return client


def test_create_config_client(config, client):
    assert (config is not None)
    assert (client is not None)
