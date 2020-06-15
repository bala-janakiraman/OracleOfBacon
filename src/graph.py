class Graph(object):

    def __init__(self):
        self.nodes = []
        self.graph = {}
        self.start = None
        self.end = None

    def addNode(self, n):
        # Add Node into Array
        self.nodes.append(n)
        title = n.value

        # Node into Dic/hash
        self.graph[title] = n

    def getNode(self, actor):
        if actor in self.graph.keys():
            return self.graph[actor]
        else:
            return None

    def setStart(self, actorName):
        if actorName in self.graph.keys():
            self.start = self.graph[actorName]
            return self.start
        else:
            return None

    def setEnd(self, actorName):
        if actorName in self.graph.keys():
            self.end = self.graph[actorName]
            return self.end
        else:
            return None
