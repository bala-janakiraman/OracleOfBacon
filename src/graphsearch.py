from src import graph
import logging


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
        return None

    logging.debug('Searching for connection between' + fromActor + ' & ' + toActor)

    queue = []

    start.parent = None
    start.searched = True
    queue.append(start)
    # nodesCompared = 1

    while len(queue) > 0:
        current = queue.pop(0)
        # print(nodesCompared)
        if current == end:
            wasFound = True
            break
        current.searched = True
        for neighbor in current.edges:
            if (not neighbor.searched):
                queue.append(neighbor)
                neighbor.parent = current
        # nodesCompared += 1

    if wasFound:
        return getBaconPath(current)
    else:
        # return 'No Connection Found between actors \'' + fromActor + '\' and \'' + toActor + '\''
        return None
