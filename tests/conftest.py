import pytest
from nornir import InitNornir


@pytest.fixture(scope="session")
def nr():
    nornir = InitNornir(
        config_file="path/to/config"
    )
    yield nornir
    nornir.close_connections()