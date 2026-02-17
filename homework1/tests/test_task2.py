from src.task2 import get_int, get_float, get_string, get_bool


def test_int():
    assert isinstance(get_int(), int)
    assert get_int() == 5


def test_float():
    assert isinstance(get_float(), float)
    assert get_float() == 5.5


def test_string():
    assert isinstance(get_string(), str)
    assert get_string() == "CS5300"


def test_bool():
    assert isinstance(get_bool(), bool)
    assert get_bool() is True

