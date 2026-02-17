def books():
    book_list = [
        ("The Cat in the Hat", "Dr. Seuss"),
        ("Green Eggs and Ham", "Dr. Seuss"),
        ("Oh, the Places You'll Go!", "Dr. Seuss"),
        ("One Fish, Two Fish, Red Fish, Blue Fish", "Dr. Seuss"),
        ("Horton Hears a Who!", "Dr. Seuss"),
    ]
    return book_list


def first_three_books():
    book_list = books()
    return book_list[:3]


def students():
    student_db = {
        "Alice": 1001,
        "Bob": 1002,
        "Charlie": 1003,
    }
    return student_db
