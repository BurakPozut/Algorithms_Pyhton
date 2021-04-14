class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def add_neighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def get_connections(self):
        return self.connectedTo.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):  # Print this vertex object
        return str(self.id)+'connected to' + str([x.id for x in self.connectedTo])


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def add_vertex(self, key):
        self.numVertices += 1
        new_vertex = Vertex(key)
        self.vertList[key] = new_vertex

    def get_vertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def add_edge(self, f, t, cost=0):   # f = From, t = to
        if f not in self.vertList:
            nv = self.add_vertex(f)
        if t not in self.vertList:
            nv = self.add_vertex(t)

        self.vertList[f].add_neighbor(self.vertList[t], cost)

    def get_vertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())  # Grab all the values and iterate through them

    def __contains__(self, n):
        return n in self.vertList


g = Graph()

for i in range(6):
    g.add_vertex(i)

print(g.vertList)

g.add_edge(0, 1, 2)

for vertex in g:
    print(vertex)
    print(vertex.get_connections())
    print('\n')
