import pytest

from cleo2_typehints.utils import typecheck


def test_typecheck_value_none_allow_none_true():
    assert typecheck(None, int, allow_none=True) == True
    assert typecheck(None, (int, str), allow_none=True) == True


def test_typecheck_value_none_allow_none_false():
    with pytest.raises(TypeError) as exc_info:
        typecheck(None, int, allow_none=False)
    assert str(exc_info.value) == "Received NoneType value but allow_none is False"
    with pytest.raises(TypeError) as exc_info:
        typecheck(None, (int, str), allow_none=False)
    assert str(exc_info.value) == "Received NoneType value but allow_none is False"


def test_typecheck_value_correct_type():
    assert typecheck(10, int) == True
    assert typecheck("string", str) == True
    assert typecheck([1, 2, 3], list) == True
    assert typecheck({"key": "value"}, dict) == True
    assert typecheck(10, (int, str)) == True
    assert typecheck("string", (int, str)) == True


def test_typecheck_value_incorrect_type():
    with pytest.raises(TypeError) as exc_info:
        typecheck(10, str)
    assert (
        str(exc_info.value)
        == "Received value with wrong type: Expected Type: 'str' - Actual Type: 'int' - Value: '10'"
    )

    with pytest.raises(TypeError) as exc_info:
        typecheck("string", int)
    assert (
        str(exc_info.value)
        == "Received value with wrong type: Expected Type: 'int' - Actual Type: 'str' - Value: 'string'"
    )

    with pytest.raises(TypeError) as exc_info:
        typecheck([1, 2, 3], dict)
    assert (
        str(exc_info.value)
        == "Received value with wrong type: Expected Type: 'dict' - Actual Type: 'list' - Value: '[1, 2, 3]'"
    )

    with pytest.raises(TypeError) as exc_info:
        typecheck({"key": "value"}, list)
    assert (
        str(exc_info.value)
        == "Received value with wrong type: Expected Type: 'list' - Actual Type: 'dict' - Value: '{'key': 'value'}'"
    )


def test_typecheck_value_correct_type_tuple():
    assert typecheck(10, (int, str)) == True
    assert typecheck("string", (int, str)) == True
    assert typecheck([1, 2, 3], (list, dict)) == True
    assert typecheck({"key": "value"}, (list, dict)) == True


def test_typecheck_value_incorrect_type_tuple():
    with pytest.raises(TypeError) as exc_info:
        typecheck(10, (str, list))
    assert (
        str(exc_info.value)
        == "Received value with wrong type: Expected Type: '(<class 'str'>, <class 'list'>)' - Actual Type: 'int' - Value: '10'"
    )

    with pytest.raises(TypeError) as exc_info:
        typecheck("string", (int, list))
    assert (
        str(exc_info.value)
        == "Received value with wrong type: Expected Type: '(<class 'int'>, <class 'list'>)' - Actual Type: 'str' - Value: 'string'"
    )

    with pytest.raises(TypeError) as exc_info:
        typecheck([1, 2, 3], (int, dict))
    assert (
        str(exc_info.value)
        == "Received value with wrong type: Expected Type: '(<class 'int'>, <class 'dict'>)' - Actual Type: 'list' - Value: '[1, 2, 3]'"
    )

    with pytest.raises(TypeError) as exc_info:
        typecheck({"key": "value"}, (int, list))
    assert (
        str(exc_info.value)
        == "Received value with wrong type: Expected Type: '(<class 'int'>, <class 'list'>)' - Actual Type: 'dict' - Value: '{'key': 'value'}'"
    )
