class Node:
    # Individual node
    def __init__(self, integer):
        self.integer = integer
        self.pointer = None


class LinkedList:
    #List of nodes

    def __init__(self):
        self.head = None
    #List has no head upon creation

    def append(self, integer):
        node = Node(integer)

        if self.head is None:

            self.head = node
            #If list is empty make first element the head

        else:

            currentInteger = self.head

            while currentInteger.pointer is not None:

                currentInteger = currentInteger.pointer
            
            currentInteger.pointer = node
            #Set pointer of previous node to next node
    
    def insert(self, integer, i):
        node = Node(integer)
        #Next node to be inserted
            
        if i == 0:

            node.pointer = self.head

            self.head = node
        #Insert into the very beginning

        else:
            backNode = None
            currentNode = self.head
            path = 0

            while currentNode is not None and path < i:
                path = path + 1

                backNode = currentNode
                currentNode = currentNode.pointer

            if path == i:
                backNode.pointer = node
                node.pointer = currentNode
    
    def delete(self, i):
        
        if self.head is None:

            return None
        
        elif i == 0:
            headHelper = self.head
            deletedInt = headHelper.integer

            self.head = headHelper.pointer

            return deletedInt
        
        else:
            path2 = 0
            node = self.head
            backNode = None

            while path2 < i and node is not None:
                path2 = path2 + 1
                
                backNode = node
                node = node.pointer
            if node is None:
                return None
            
            deletedInt = node.integer
            if backNode is None:
                self.head = node.pointer

            else:
                backNode.pointer = node.pointer
            
            return deletedInt

    def print(self):
        i = self.head

        while i is not None:
            if i.pointer is not None:
                arrow = " -> "
            else:
                arrow = ""

            print(f"{i.integer}{arrow}", end='')

            i = i.pointer

        print("")

    def index(self, input):
        i = 0
        node = self.head

        while node is not None:
            if input == node.integer:
                return i
            else:
                i = i+1
                node = node.pointer
        return -1

    def swap(self, input1, input2):
        i = 0
        j = 0
        int1 = None
        int2 = None
        node = self.head

        while node is not None:
            if input1 == i:
                int1 = node.integer

            node = node.pointer
            i = i+1
        node = self.head
        while node is not None:
            if input2 == j:
                int2 = node.integer

            node = node.pointer
            j = j+1
        
        if int1 is not None and int2 is not None:
            node = self.head
            counter = 0
            while node is not None:
                if counter == input1:
                    node.integer = int2
                    
                elif counter == input2:
                    node.integer = int1
                node = node.pointer
                counter = counter+1

                
if __name__ == "__main__":
    L = LinkedList()
    for num in (3, 5, 2, 7, 8, 10, 6):
        L.append(num)
    L.print()           # 3 -> 5 -> 2 -> 7 -> 8 -> 10 -> 6
    print(L.index(7))   # 3
    print(L.index(9))   # -1
    L.swap(1, 4)
    L.print()           # 3 -> 8 -> 2 -> 7 -> 5 -> 10 -> 6
    L.swap(2, 0)
    L.print()           # 2 -> 8 -> 3 -> 7 -> 5 -> 10 -> 6
