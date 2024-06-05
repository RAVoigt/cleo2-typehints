import pytest

from typehints_cleo2.utils import nonecheck


def test_nonecheck_value_not_none():
    assert nonecheck(10) == False
    assert nonecheck("string") == False
    assert nonecheck([1, 2, 3]) == False
    assert nonecheck({"key": "value"}) == False
    assert nonecheck(0) == False
    assert nonecheck("") == False


def test_nonecheck_value_none_allow_none_true():
    assert nonecheck(None, allow_none=True) == True


def test_nonecheck_value_none_allow_none_false():
    with pytest.raises(TypeError) as exc_info:
        nonecheck(None, allow_none=False)
    assert str(exc_info.value) == "Received NoneType value but allow_none is False"


def test_nonecheck_value_none_default_allow_none():
    with pytest.raises(TypeError) as exc_info:
        nonecheck(None)
    assert str(exc_info.value) == "Received NoneType value but allow_none is False"


def test_nonecheck_value_not_none_allow_none_true():
    assert nonecheck(10, allow_none=True) == False
    assert nonecheck("string", allow_none=True) == False
    assert nonecheck([1, 2, 3], allow_none=True) == False
    assert nonecheck({"key": "value"}, allow_none=True) == False
    assert nonecheck(0, allow_none=True) == False
    assert nonecheck("", allow_none=True) == False
