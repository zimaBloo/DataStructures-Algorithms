class Graph:
    def __init__(self, n):
        self.n = n

        self.graphWhole = {}
        for i in range(n):
            self.graphWhole[i] = {}

    def add(self, u, v, w):
        self.graphWhole[u][v] = w

    def remove(self, u, v):
        if v in self.graphWhole[u]:
            del self.graphWhole[u][v] #This website helped me to understand how to remove an entry: https://www.freecodecamp.org/news/python-remove-key-from-dictionary/#:~:text=You%20can%20do%20so%20using,value%20pair%20in%20a%20dictionary.

    def shortest_path(self, start, end):
        distances = {}
        for vertex in self.graphWhole:
            distances[vertex] = float('inf') #learned on this website: https://www.geeksforgeeks.org/python-infinity/

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

            for neighbor, weight in self.graphWhole[currentVert].items(): #.items method for returning tuples was learned here https://www.w3schools.com/python/python_ref_dictionary.asp
                totalDist = currentDist + weight

                if totalDist < distances[neighbor]:
                    distances[neighbor] = totalDist

                    prevVert[neighbor] = currentVert


                    sequence.append((totalDist, neighbor))



        path = []
        current = end

        if distances[end] == float('inf'):
           print(-1)
           return

        while current is not None:

            path.append(current)

            current = prevVert[current]


        path.reverse()

        for i in path:
            print(i, end=' ')
        print()

        path.reverse()



if __name__ == "__main__":

    graph = Graph(6)

    connections = ((0, 1, 24), (0, 2, 13),
                (1, 5,  9), (2, 5, 19),
                (3, 0, 25), (4, 0, 20),
                (5, 3, 18), (5, 4, 36))

    for u, v, w in connections:
        graph.add(u, v, w)

    graph.shortest_path(0, 3)
    graph.shortest_path(3, 1)
    graph.shortest_path(2, 4)

    graph.remove(0, 2)
    graph.remove(3, 0)

    graph.shortest_path(0, 3)
    graph.shortest_path(3, 1)
    graph.shortest_path(2, 4)