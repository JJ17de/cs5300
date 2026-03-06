Feature: Movie Theater Booking
  Users should be able to browse movies, book seats, and check their bookings

  Scenario: See all the movies
    Given some movies have been added
    When I go to the main page
    Then I should see the movie names on the page

  Scenario: No movies to show
    Given no movies exist yet
    When I go to the main page
    Then I should see a message saying no movies are available

  Scenario: Book a seat for a movie
    Given a movie exists and there are open seats
    When I pick a seat and book it
    Then that seat should show as booked
    And my booking should show up in the system

  Scenario: Check my booking history
    Given I already have a booking
    When I go to the booking history page
    Then I should see my booking info on the page

  Scenario: Get movies from the API
    Given some movies have been added
    When I hit the movies API endpoint
    Then I should get back a list of movies as JSON

  Scenario: Add a movie through the API
    When I send a new movie to the API
    Then the movie should get created