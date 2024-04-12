import heapq

class Vertex:
        def __init__(self, name):
            self.name = name
            self.adjacent_vertices = []
            self.visited = False
            self.shortest_distance = float('inf')

        def add_adjacent_vertex(self, adjacent_vertex, weight):
            self.adjacent_vertices.append((adjacent_vertex, weight))
        
        def __lt__(self, other):
            return self.shortest_distance < other.shortest_distance

class Graph:
        def __init__(self):
            self.vertices = []
            self.edges = []

        def add_vertex(self, vertex):
            self.vertices.append(vertex)

class FlightAgency:
        def __init__(self):
            self.graph = Graph()

        def add_vertex(self, vertex):
            self.graph.add_vertex(vertex)

        def add_edge(self, start_vertex, end_vertex, weight):
            start_vertex.add_adjacent_vertex(end_vertex, weight)
            self.graph.edges.append((start_vertex, end_vertex))

        def dijkstra(self, start_vertex):
            q = []
            start_vertex.shortest_distance = 0
            heapq.heappush(q, start_vertex)

            while len(q) > 0:
                actual_vertex = heapq.heappop(q)

                for adjacent_vertex, weight in actual_vertex.adjacent_vertices:
                    if adjacent_vertex.visited == False:
                        tentative_distance = actual_vertex.shortest_distance + weight

                        if tentative_distance < adjacent_vertex.shortest_distance:
                            adjacent_vertex.shortest_distance = tentative_distance
                            heapq.heappush(q, adjacent_vertex)

                actual_vertex.visited = True

        def earliest_arrival_time(self, start_vertex, end_vertex):
            self.dijkstra(start_vertex)
            return end_vertex.shortest_distance