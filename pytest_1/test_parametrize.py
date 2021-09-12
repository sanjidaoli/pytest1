import pytest

@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+5",7),("7*5",35)])
def test_eval(test_input,expected):
    assert eval(test_input) == expected
