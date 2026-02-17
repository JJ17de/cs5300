from src.task3 import check_number, prime, sum_numbers


def test_positive():
    assert check_number(1) == "positive"


def test_negative():
    assert check_number(-1) == "negative"


def test_zero():
    assert check_number(0) == "zero"


def test_primes():
    result = prime()

    assert result[0] == 2
    assert result[1] == 3
    assert result[2] == 5
    assert len(result) == 10


def test_sum_numbers():
    assert sum_numbers() == 5050

