from src import setupgraph
from src import graph

# Get Kevin Bacon metrics - Bacon #, Bacon Path etc
def getBaconPath(end_node):
    path = []
    pathTxt = ''
    path.append(end_node)
    nextNode = end_node.parent
    while nextNode is not None:
        path.append(nextNode)
        nextNode = nextNode.parent

    for node in path:
        pathTxt += node.value
        if node.parent is not None:
            pathTxt = pathTxt + '-->'
    return pathTxt


# Breadth First Search
def bfs(graph: graph, fromActor, toActor):
    wasFound = False
    start = graph.setStart(fromActor)  # Kevin bacon
    end = graph.setEnd(toActor)  # target actor

    if end is None or start is None:
        print('Actors not found')
        return None

    queue = []

    start.parent = None
    start.searched = True
    queue.append(start)

    while len(queue) > 0:
        current = queue.pop(0)
        if current == end:
            print('Found \'' + current.value + '\'')
            wasFound = True
            break
        current.searched = True
        for neighbor in current.edges:
            if (not neighbor.searched):
                queue.append(neighbor)
                neighbor.parent = current

    if wasFound:
        return getBaconPath(current)
    else:
        return 'No Connection Found between actors \'' + fromActor + '\' and \'' + toActor + '\''

# Dataset 1
# dataSetFilename = "data/KevinBacon.json"

# Data set 2
dataSetFilename = "data/imdbData.json"

# Set up the graph with Movie - Actor data
graph = setupgraph.setupGraph(dataSetFilename)

#for Dataset 1
# print(bfs(graph, "Kevin Bacon", "Jim Carrey"))

# for Dataset2
print(bfs(graph, "Jack Nicholson", "Jan Fedder"))

