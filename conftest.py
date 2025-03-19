import pytest

@pytest.fixture(scope='session')
def pre_work():
    print("session scope ")
    return 'pass'
