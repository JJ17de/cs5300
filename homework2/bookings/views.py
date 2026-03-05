from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})


def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.all()

    if request.method == 'POST':
        seat_id = request.POST.get('seat_id')
        seat = get_object_or_404(Seat, id=seat_id)

        if seat.booking_status:
            messages.error(request, 'That seat is already booked.')
            return redirect('book_seat', movie_id=movie.id)

        user = User.objects.first()
        if not user:
            user = User.objects.create_user(username='guest', password='guest123')

        Booking.objects.create(movie=movie, seat=seat, user=user)
        seat.booking_status = True
        seat.save()

        messages.success(request, f'Seat {seat.seat_number} booked for {movie.title}!')
        return redirect('booking_history')

    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})


def booking_history(request):
    bookings = Booking.objects.select_related('movie', 'seat', 'user').order_by('-booking_date')
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})