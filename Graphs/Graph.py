from enum import Enum
from collections import OrderedDict


class State(Enum):
    unvisited = 1
    visited = 2
    visiting = 3


class Node:
    def __init__(self, num):
        self.num = num
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict()  # Remembers the order that keys were first inserted

    def __str__(self):
        return str(self.num)


class Graph:
    def __init__(self):
        self.nodes = OrderedDict()

    def add_node(self, num):
        node = Node(num)
        self.nodes[num] = node
        return node

    def add_edge(self, source, destination, weight=0):
        if source not in self.nodes:
            self.add_node(source)
        if destination not in self.nodes:
            self.add_node(destination)
        self.nodes[source].adjacent[self.nodes[destination]] = weight


g = Graph()
g.add_edge(0, 1, 10)    # This already checks if node is exist if its not then this func. will call add_node func.
print(g.nodes)
g.add_edge(1, 2, 3)
print(g.nodes)

