class Graph:
    def __init__(self, n):
        self.n = n

        self.bothEdges = {}
        for i in range(n):
            self.bothEdges[i] = set()

    def add(self, u, v):
        # Undirected edge
        # Add method usage learned on https://www.w3schools.com/python/python_ref_set.asp
        self.bothEdges[u].add(v)
        self.bothEdges[v].add(u)

    def remove(self, u, v):
        # Discard method learned on https://www.w3schools.com/python/python_ref_set.asp
        if self.bothEdges[u] is not None:
            self.bothEdges[u].discard(v)
        if self.bothEdges[v] is not None:
            self.bothEdges[v].discard(u)

    def dft(self, start):
            revQue = [start]
            visitedVrtx = set()

            while len(revQue) > 0:
                current = revQue.pop()

                if current not in visitedVrtx:
                    
                    visitedVrtx.add(current)
                    print(f"{current} ", end='')

                    nearby = []

                    for i in sorted(self.bothEdges[current], reverse=True): #Wont work otherwise, reverse for correct printing
                        if i not in visitedVrtx:
                            nearby.append(i)

                    revQue.extend(nearby)

            print('\n')

    def bft(self, start):
        que = [start]
        visitedVrtx = set()

        while len(que) > 0:
            current = que.pop(0)

            if current not in visitedVrtx:

                print(f"{current} ", end='')

                visitedVrtx.add(current)
                
                notVisited = sorted(self.bothEdges[current] - visitedVrtx)
                que.extend(notVisited)
        
        print('\n')

if __name__ == "__main__":
    graph = Graph(6)
    edges = ((0, 2), (0, 4), (2, 1),
             (2, 3), (2, 5), (3, 0),
             (3, 5), (4, 5), (5, 1))
    for u, v in edges:
        graph.add(u, v)
        
    graph.dft(0)           # 0 2 1 5 3 4 
    graph.bft(0)           # 0 2 3 4 1 5 

    graph.remove(0, 2)
    graph.remove(2, 5)
    graph.remove(1, 4)

    graph.dft(0)           # 0 3 2 1 5 4 
    graph.bft(0)           # 0 3 4 2 5 1 
