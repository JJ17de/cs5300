from src.task4 import discount


def test_int():
    assert discount(100, 10) == 90


def test_float():
    assert discount(100.0, 20.0) == 80.0


def test_mixed():
    assert discount(100, 30.0) == 70.0


