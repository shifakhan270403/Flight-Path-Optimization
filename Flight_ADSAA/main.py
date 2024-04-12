from flight import FlightAgency, Vertex

def run():
        flight_agency = FlightAgency()

        airport_a = Vertex('A')
        airport_b = Vertex('B')
        airport_c = Vertex('C')
        airport_d = Vertex('D')
        airport_e = Vertex('E')

        flight_agency.add_vertex(airport_a)
        flight_agency.add_vertex(airport_b)
        flight_agency.add_vertex(airport_c)
        flight_agency.add_vertex(airport_d)
        flight_agency.add_vertex(airport_e)

        flight_agency.add_edge(airport_a, airport_b, 1)
        flight_agency.add_edge(airport_a, airport_c, 4)
        flight_agency.add_edge(airport_b, airport_d, 2)
        flight_agency.add_edge(airport_c, airport_d, 1)
        flight_agency.add_edge(airport_d, airport_e, 3)

        print(f'The earliest arrival time from airport A to airport E is {flight_agency.earliest_arrival_time(airport_a, airport_e)}')

if __name__ == '__main__':
        run()