# Methods add(), remove() and shortest_path() were taken from my last weeks implementation.

class Graph:
    def __init__(self, n):
        self.n = n

        self.graphWhole = {}
        for i in range(n):
            self.graphWhole[i] = {}

    def add(self, u, v, w):
        if 0 <= u and u < self.n:
            if 0 <= v and v < self.n:
                self.graphWhole[u][v] = w

    def remove(self, u, v):
        if v in self.graphWhole[u]:
            del self.graphWhole[u][v] 

    def shortest_path(self, start, end):
        distances = {}
        for vertex in self.graphWhole:
            distances[vertex] = float('inf')

        prevVert = {}
        for vertex2 in self.graphWhole:
            prevVert[vertex2] = None

        distances[start] = 0

        sequence = [(0, start)]

        while len(sequence) > 0:
            minDist = float('inf')
            minVert = None
            
            for d, v in sequence:
                if d < minDist:
                    minDist = d
                    minVert = v
            currentDist = minDist
            currentVert = minVert

            sequence.remove((currentDist, currentVert))

            if currentVert == end:
                break

            for neighbor, weight in self.graphWhole[currentVert].items():
                totalDist = currentDist + weight

                if totalDist < distances[neighbor]:
                    distances[neighbor] = totalDist

                    prevVert[neighbor] = currentVert


                    sequence.append((totalDist, neighbor))



        path = []
        current = end

        if distances[end] == float('inf'):
           return -1

        while current is not None:

            path.append(current)

            current = prevVert[current]


        path.reverse()

        return distances[end]


    def all_paths(self):
        dists = []
        
        for discard in range(self.n):
            singleRow = [float('inf')] * self.n

            dists.append(singleRow)

        for i in range(self.n):

            for j in range(self.n):
                shortest = self.shortest_path(i, j)
                dists[i][j] = shortest

                if dists[i][j] == float('inf'):
                    dists[i][j] = -1

        return dists



graph = Graph(6)

connections = (( 1,  2, 17), ( 4,  6, 14), ( 2,  5, 15),
               ( 3,  4,  3), ( 0,  5, 18), ( 3,  5,  8),
               ( 2,  0,  9), ( 0,  2, 19), ( 0,  1, 10),
               ( 1,  0, 13), ( 4,  1, 12), ( 5,  1,  3))

for u, v, w in connections:
    graph.add(u, v, w)

A = graph.all_paths()

for row in A:
    print(row)

print()
graph.remove(3, 4)
graph.remove(1, 0)
graph.remove(4, 1)

A = graph.all_paths()
for row in A:
    print(row)