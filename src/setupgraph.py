from src.graph import Graph
from src.node import Node
import json


def preload(dataSetFilename):
    with open(dataSetFilename, 'r') as dataSet:
        data = json.load(dataSet)
    return data


def setupGraph(dataSetFilename):
    graph = Graph()
    data = preload(dataSetFilename)
    movies = data['movies']

    for movie in movies:
        movieTitle = movie['title']
        cast = movie['cast']

        movieNode = Node(movieTitle)
        graph.addNode(movieNode)

        for actor in cast:
            actorNode = graph.getNode(actor)
            if actorNode == None:
                actorNode = Node(actor)
                graph.addNode(actorNode)
            movieNode.addEdges(actorNode)

    return graph
