import unittest
from flight import FlightAgency, Vertex

class TestFlight(unittest.TestCase):

        def setUp(self):
            self.flight_agency = FlightAgency()

            self.airport_a = Vertex('A')
            self.airport_b = Vertex('B')
            self.airport_c = Vertex('C')
            self.airport_d = Vertex('D')
            self.airport_e = Vertex('E')

            self.flight_agency.add_vertex(self.airport_a)
            self.flight_agency.add_vertex(self.airport_b)
            self.flight_agency.add_vertex(self.airport_c)
            self.flight_agency.add_vertex(self.airport_d)
            self.flight_agency.add_vertex(self.airport_e)

            self.flight_agency.add_edge(self.airport_a, self.airport_b, 1)
            self.flight_agency.add_edge(self.airport_a, self.airport_c, 4)
            self.flight_agency.add_edge(self.airport_b, self.airport_d, 2)
            self.flight_agency.add_edge(self.airport_c, self.airport_d, 1)
            self.flight_agency.add_edge(self.airport_d, self.airport_e, 3)

        def test_earliest_arrival_time(self):
            self.assertEqual(self.flight_agency.earliest_arrival_time(self.airport_a, self.airport_e), 7)

if __name__ == '__main__':
        unittest.main()