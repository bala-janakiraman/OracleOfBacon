class Node:

    def __init__(self, value):
        self.value = value
        self.edges = []
        self.searched = False
        self.parent = None

    def addEdges(self, neighbor):
        # current node pointing to neighbor
        self.edges.append(neighbor)
        # neighbor pointing to  current node
        neighbor.edges.append(self)
