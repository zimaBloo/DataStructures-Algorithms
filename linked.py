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
            
            if backNode is None:
                self.head = node.pointer

            else:
                backNode.pointer = node.pointer

            deletedInt = node.integer
            
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

if __name__ == "__main__":
    L = LinkedList()
    L.append(1)
    L.append(3)
    L.print()           # 1 -> 3
    L.insert(10, 1)
    L.insert(15, 0)
    L.print()           # 15 -> 1 -> 10 -> 3
    L.delete(0)
    L.print()           # 1 -> 10 -> 3
