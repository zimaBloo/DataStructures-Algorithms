# Methods and some code were taken from my last weeks implementation of the exercises

class Graph:
    def __init__(self, n):
        self.n = n

        self.graphWhole = {}
        for i in range(n):
            self.graphWhole[i] = {}

    def add(self, u, v, w):
        if 0 <= u and u < self.n and 0 <= v and v < self.n:
            self.graphWhole[u][v] = w
            self.graphWhole[v][u] = w

    def remove(self, u, v):
        if v in self.graphWhole[u]:
            del self.graphWhole[u][v]
        if u in self.graphWhole[v]:
            del self.graphWhole[v][u]

    def min_expense(self):
        cumulativeWeight = 0

        visited = []
        for discard in range(self.n):
            visited.append(False)


        for s in range(self.n):
            if visited[s] == False:
                allEdges = []
                allEdges.append((0,s))

                while allEdges:
                    minWeight = float('inf')

                    for weight, vertex in allEdges:
        
                        if weight < minWeight:
                            minWeight = weight
                            u = vertex


                    allEdges.remove((minWeight, u))

                    if visited[u] == False:
                        
                        cumulativeWeight = cumulativeWeight + minWeight


                        visited[u] = True
            

                        for j in self.graphWhole[u].items(): # items() method was lerned here: https://www.w3schools.com/python/ref_dictionary_items.asp
                            v, w = j

                            if visited[v] == False:
                                allEdges.append((w, v))


        return cumulativeWeight
    
    
graph = Graph(6)

connections = (( 1,  2, 17), ( 4,  6, 14), ( 2,  5, 15),
               ( 3,  4,  3), ( 0,  5, 18), ( 3,  5,  8),
               ( 2,  0,  9), ( 0,  2, 19), ( 0,  1, 10),
               ( 1,  0, 13), ( 4,  1, 12), ( 5,  1,  3))

for u, v, w in connections:
    graph.add(u, v, w)

print(graph.min_expense())

graph.remove(3, 4)
graph.remove(1, 0)
graph.remove(4, 1)

print(graph.min_expense())