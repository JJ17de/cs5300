from behave import given, when, then
from django.contrib.auth.models import User
from bookings.models import Movie, Seat, Booking
from datetime import date
import json


@given('some movies have been added')
def step_create_movies(context):
    context.movie = Movie.objects.create(
        title="F1 The Movie",
        description="one of the greatest movies of all time",
        release_date=date(2025, 6, 27),
        duration=155
    )


@given('no movies exist yet')
def step_no_movies(context):
    Movie.objects.all().delete()


@when('I go to the main page')
def step_visit_main(context):
    context.response = context.test.client.get('/')


@then('I should see the movie names on the page')
def step_see_movies(context):
    assert context.response.status_code == 200
    assert 'F1 The Movie' in context.response.content.decode()


@then('I should see a message saying no movies are available')
def step_no_movies_message(context):
    assert context.response.status_code == 200
    assert 'No movies available' in context.response.content.decode()


@given('a movie exists and there are open seats')
def step_movie_and_seats(context):
    context.movie = Movie.objects.create(
        title="Bad Boys",
        description="Again, one of the greatest movies of all time",
        release_date=date(1995, 4, 7),
        duration=119
    )
    context.seat = Seat.objects.create(seat_number="E5", booking_status=False)


@when('I pick a seat and book it')
def step_book_seat(context):
    context.response = context.test.client.post(
        f'/book/{context.movie.id}/',
        {'seat_id': context.seat.id}
    )


@then('that seat should show as booked')
def step_seat_booked(context):
    context.seat.refresh_from_db()
    assert context.seat.booking_status is True


@then('my booking should show up in the system')
def step_booking_exists(context):
    assert Booking.objects.count() >= 1


@given('I already have a booking')
def step_existing_booking(context):
    user = User.objects.create_user(username="testuser", password="testpass123")
    movie = Movie.objects.create(
        title="The Equalizer",
        description="another great movie",
        release_date=date(2014, 9, 26),
        duration=132
    )
    seat = Seat.objects.create(seat_number="D4", booking_status=True)
    Booking.objects.create(movie=movie, seat=seat, user=user)


@when('I go to the booking history page')
def step_visit_history(context):
    context.response = context.test.client.get('/history/')


@then('I should see my booking info on the page')
def step_see_booking(context):
    assert context.response.status_code == 200
    assert 'The Equalizer' in context.response.content.decode()


@when('I hit the movies API endpoint')
def step_hit_api(context):
    context.response = context.test.client.get('/api/movies/')


@then('I should get back a list of movies as JSON')
def step_movies_json(context):
    assert context.response.status_code == 200
    data = json.loads(context.response.content)
    assert len(data) >= 1


@when('I send a new movie to the API')
def step_post_movie(context):
    context.response = context.test.client.post(
        '/api/movies/',
        data=json.dumps({
            "title": "2 Fast 2 Furious",
            "description": "The best movie in the fast and furious franchise",
            "release_date": "2003-06-06",
            "duration": 107
        }),
        content_type='application/json'
    )


@then('the movie should get created')
def step_movie_created(context):
    assert context.response.status_code == 201