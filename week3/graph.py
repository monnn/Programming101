class DirectedGraph:
    def __init__(self):
        self.nodes_list = {}
        self.values_list = []

    def addEdge(self, nodeA, nodeB):
        if nodeA not in self.nodes_list:
            self.values_list = []
        self.values_list.append(nodeB)
        self.nodes_list.update({nodeA: self.values_list})

    def getNeighborsFor(self, node):
        neighbors = self.nodes_list.get(node)
        return neighbors

    def pathBetween(self, nodeA, nodeB):
        if nodeA not in self.nodes_list or nodeB not in self.nodes_list:
            return False
        if nodeB in self.nodes_list.get(nodeA):
            return True
        for node in self.nodes_list.get(nodeA):
            if self.pathBetween(node, nodeB):
                return True
        return False

    def toString(self):
        return str(self.nodes_list)

graph = DirectedGraph()
graph.addEdge("Ani", "Bon")
graph.addEdge("Ani", "Ton")
graph.addEdge("Ton", "Mon")
graph.addEdge("Bon", "Sani")
graph.addEdge("Sani", "Geni")
graph.addEdge("Geni", "Keni")
print(graph.pathBetween("Ani", "Geni"))
#print(graph.toString())
#print(graph.getNeighborsFor("Ani"))
