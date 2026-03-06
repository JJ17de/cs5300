from django.test import TestCase
from .models import Movie, Seat, Booking
from django.contrib.auth.models import User
from datetime import date
from rest_framework.test import APITestCase
from rest_framework import status


class MovieModelTest(TestCase):

    def setUp(self):
        self.movie = Movie.objects.create(
            title="F1 The Movie",
            description="One of the greatest movies of all time",
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

class BookingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.movie = Movie.objects.create(
            title="Bad Boys",
            description="Again, one of the greatest movies of all time",
            release_date=date(1995, 4, 7),
            duration=119
        )
        self.seat = Seat.objects.create(seat_number="D4", booking_status=False)
        self.booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.movie, self.movie)
        self.assertEqual(self.booking.seat, self.seat)
        self.assertEqual(self.booking.user, self.user)

    def test_booking_str(self):
        self.assertIn("testuser", str(self.booking))
        self.assertIn("Bad Boys", str(self.booking))

    def test_booking_date_auto(self):
        self.assertIsNotNone(self.booking.booking_date)


class MovieViewSetTest(APITestCase):

    def setUp(self):
        self.movie = Movie.objects.create(
            title="The Equalizer",
            description="Again, another one of the greatest movies of all time, trust me bro",
            release_date="2014-09-26",
            duration=132
        )

    def test_list_movies(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)