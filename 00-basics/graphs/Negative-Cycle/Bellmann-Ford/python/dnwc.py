# Belmann Ford Algorithm

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, source, destination, weight):
        self.graph.append([source, destination, weight])

    def print_solution(self, distance):
        print("Vertex Distance from Source")
        for i in range(self.vertices):
            print("{0}\t\t{1}".format(i, distance[i]))

    def belmann_ford(self, source):

        # fill the distance array and predecessor array
        distance = [float("inf")] * self.vertices
        # mark the source vertex
        distance[source] = 0

        # relax edges |vertices| - 1 times
        for _ in range(self.vertices - 1):
            for source, destination, weight in self.graph:
                if distance[source] != float("inf") and distance[source] + weight < distance[destination]:
                    print("Graph contains negative edge cycle")
                    return
        # no negative weight cycle found !
        # print the distance and predecessor array
        self.print_solution(distance)


g = Graph(5)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 3)
g.add_edge(2, 1, 6)
g.add_edge(3, 2, 2)

g.belmann_ford(0)
