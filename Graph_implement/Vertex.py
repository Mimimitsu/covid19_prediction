# Vertex使用字典connectedTo来记录与其相连的顶点, 以及每一条边的权重
class Vertex():
    # Initialization of the id, and the dictionary connectedTo
    def __init__(self, key) -> None:
        self.id = key
        self.connectedTo = {}

    # Connect one vertex to another vertex
    def addNeighbor(self, nbr, weight = 0) -> None:
        self.connectedTo[nbr] = weight

    def __str__(self) -> str:
        return str(self.id) + ': connectedTo: ' + str([x.id for x in self.connectedTo])

    # Return all the connected vertices of this vertex
    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    # Return the weights of one neighbour
    def getWeight(self, nbr):
        return self.connectedTo[nbr]