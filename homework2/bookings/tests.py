from django.test import TestCase
from .models import Movie, Seat
from datetime import date



class MovieModelTest(TestCase):

    def setUp(self):
        self.movie = Movie.objects.create(
            title="F1 The Movie",
            description="one of the greatest movies of all time",
            release_date=date(2025, 6, 27),
            duration=155
        )

    def test_movie_creation(self):
        self.assertEqual(self.movie.title, "F1 The Movie")
        self.assertEqual(self.movie.duration, 155)

    def test_movie_str(self):
        self.assertEqual(str(self.movie), "F1 The Movie")

class SeatModelTest(TestCase):

    def setUp(self):
        self.seat = Seat.objects.create(seat_number="E5", booking_status=False)

    def test_seat_creation(self):
        self.assertEqual(self.seat.seat_number, "E5")
        self.assertFalse(self.seat.booking_status)

    def test_seat_str(self):
        self.assertEqual(str(self.seat), "E5")

    def test_seat_default_status(self):
        seat = Seat.objects.create(seat_number="F6")
        self.assertFalse(seat.booking_status)