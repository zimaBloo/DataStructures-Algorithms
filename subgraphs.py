#Most of the exercise was taken from my last weeks submission, including add(), remove(), and dtf() methods, where almost whole dft() method was used in subgraphs() method.

class Graph:
    def __init__(self, n):
        self.n = n

        self.bothEdges = {}
        for i in range(n):
            self.bothEdges[i] = set()

    def add(self, u, v):
        self.bothEdges[u].add(v)
        self.bothEdges[v].add(u)

    def remove(self, u, v):
        if self.bothEdges[u] is not None:
            self.bothEdges[u].discard(v)
        if self.bothEdges[v] is not None:
            self.bothEdges[v].discard(u)

    def subgraphs(self):
        visitedVrtx = set()
        counter = 0

        for i in range(self.n):
            
            if i not in visitedVrtx:
                revQue = [i]

                while len(revQue) > 0:
                    current = revQue.pop()

                    if current not in visitedVrtx:
                        
                        visitedVrtx.add(current)

                        nearby = []

                        for i in sorted(self.bothEdges[current], reverse=True):
                            if i not in visitedVrtx:
                                nearby.append(i)

                        revQue.extend(nearby)
                
                counter += 1

        return counter


if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 4), (2, 1),
             (2, 5), (3, 0),
             (5, 1))
    for u, v in edges:
        graph.add(u, v)
    
    print(graph.subgraphs())  # 2
    
    more_connections = ((0, 2), (2, 3),
                        (3, 5), (4, 5))
    for u, v in more_connections:
        graph.add(u, v)

    print(graph.subgraphs())  # 1