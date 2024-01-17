class MinHeap:
    def __init__(self, A):
        self.heap = A
        self.createHeap()

    def createHeap(self):
        ind = int((len(self.heap) - 1) / 2)

        while ind >= 0:
            self.algorithm(ind)
            ind = ind - 1

    def getValue(self, index):
        if index < len(self.heap):
            return self.heap[index]
    
    def algorithm(self, i):
        smallestInd = i

        conditionLeftChild = 2 * i + 1
        conditionRightChild = 2 * i + 2

        potentialMins = [i]
        if conditionRightChild < len(self.heap) and self.heap[conditionRightChild] < self.heap[smallestInd]:
            potentialMins.append(conditionRightChild)
        if conditionLeftChild < len(self.heap) and self.heap[conditionLeftChild] < self.heap[smallestInd]:
            potentialMins.append(conditionLeftChild)

        helper = self.getValue
        #Usage of key argument was learned on: https://note.nkmk.me/en/python-key-sort-sorted-max-min/
        smallestInd = min(potentialMins, key = helper)

        if smallestInd != i:
            helper2 = self.heap[i]
            self.heap[i] = self.heap[smallestInd]
            self.heap[smallestInd] = helper2
            self.algorithm(smallestInd)

    def push(self, key: int):
        self.heap.append(key)

        i = len(self.heap) - 1
        pNode = (i - 1) // 2
        while i > 0 and self.heap[pNode] > self.heap[i]:

            self.heap[i], self.heap[pNode] = self.heap[pNode], self.heap[i]

            i = pNode
            pNode = (i - 1) // 2

    def pop(self):
        smallest = self.heap[0]
        self.heap[0] = self.heap[-1]

        helper4 = []
        for i in range(len(self.heap) - 1):
            helper4.append(self.heap[i])
        self.heap = helper4
        
        self.algorithm(0)
        return smallest

    def print(self):
        string = ""
        for i in self.heap:
            string = string + str(i) + " "
        print(string)
        
if __name__ == "__main__":
    heap = MinHeap([4, 8, 6, 5, 1, 2, 3])
    heap.print()        # 1 4 2 5 8 6 3 
    print(heap.pop())   # 1
    heap.push(9)
    heap.print()        # 2 4 3 5 8 6 9