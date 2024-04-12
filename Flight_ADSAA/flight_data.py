import csv

class Flight:
        def __init__(self, flight_number, origin, destination, departure_time, arrival_time):
            self.flight_number = flight_number
            self.origin = origin
            self.destination = destination
            self.departure_time = departure_time
            self.arrival