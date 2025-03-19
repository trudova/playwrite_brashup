import pytest

@pytest.fixture(scope='module')
def pre_work2():
    print("before module")
    return 'pass'

@pytest.fixture(scope='function')
def pre_work3():
    print("start of driver")
    yield
    print('teardown of driver!!!')

@pytest.mark.smoke
def test_initial_check(pre_work,pre_work2,pre_work3):
    0 ==False
    assert pre_work2 == 'pass'

def test_second_check(pre_work,pre_work3):
    0 ==False

@pytest.mark.skip
def test_second_check2(pre_work,pre_work3):
    0 ==False