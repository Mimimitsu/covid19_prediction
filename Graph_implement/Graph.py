from Vertex import Vertex

class Graph():
    def __init__(self) -> None:
        self.verList = {}
        self.numVertices = 0

    def addVertex(self, key) -> Vertex:
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        if self.__contains__(key):
            return None
        else:
            self.verList[key] = newVertex
            return newVertex

    def getVertex(self, n) -> Vertex:
        if n in self.verList:
            return self.verList[n]
        else:
            return None

    def __contains__(self, key) -> Vertex:
        return key in self.verList

    def addEdge(self, f: str, t: str, weight = 0):
        if self.__contains__(f) == False:
            nv = self.addVertex(f)
        if self.__contains__(t) == False:
            nv = self.addVertex(t)
        self.verList[f].addNeighbor(self.verList[t], weight)

    def getVertices(self):
        return self.verList.keys()

    def __iter__(self):
        return iter(self.verList.values())
