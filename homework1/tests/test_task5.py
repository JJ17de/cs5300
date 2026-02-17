from src.task5 import books, first_three_books, students


def test_books():
    b = books()
    assert isinstance(b, list)
    assert len(b) >= 3
    assert b[0][1] == "Dr. Seuss"


def test_first_three_books():
    first_three = first_three_books()
    assert len(first_three) == 3
    assert first_three[0][0] == "The Cat in the Hat"


def test_students():
    db = students()
    assert isinstance(db, dict)
    assert db["Alice"] == 1001

