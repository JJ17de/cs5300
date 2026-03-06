# Movie Theater Booking App

You can add/delete/browse movies, book seats, and check your booking history. It also has a full REST API for everything.

## Live Site

https://hw2-movietheater.onrender.com

## What it does

- View all available movies
- Pick a seat and book it for a movie
- See all your past bookings
- Full API to create, read, update, and delete movies, seats, and bookings

## Built with

- Python / Django
- Django REST Framework
- Bootstrap 5 for the frontend
- SQLite for the database
- Deployed on Render with Gunicorn and WhiteNoise

## How to run it locally

Clone the repo and cd into homework2:
```
git clone <repo-url>
cd homework2
```

Set up a virtual environment and install everything:
```
python3 -m venv myenv --system-site-packages
source myenv/bin/activate
pip install -r requirements.txt
```

Run migrations and start the server:
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:3000
```

If you want admin access, create a superuser:
```
python3 manage.py createsuperuser
```

## API Endpoints

- `/api/movies/` - movies (CRUD)
- `/api/seats/` - seats (CRUD)
- `/api/bookings/` - bookings (CRUD)

## Running the tests

Unit and integration tests:
```
python3 manage.py test bookings
```

BDD tests:
```
python3 manage.py behave
```

## Project structure

```
homework2/
├── bookings/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── admin.py
│   ├── tests.py
│   ├── templates/bookings/
│   │   ├── base.html
│   │   ├── movie_list.html
│   │   ├── seat_booking.html
│   │   └── booking_history.html
│   └── static/bookings/
│       └── styles.css
├── movie_theater_booking/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── features/
│   ├── movies.feature
│   └── steps/
│       └── movie_steps.py
├── build.sh
├── manage.py
└── requirements.txt
```