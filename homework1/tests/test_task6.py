from src.task6 import count_words


def test_word_count():
    result = count_words("task6_read_me.txt")
    assert isinstance(result, int)
    assert result > 0

