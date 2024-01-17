class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None


    def insert(self, key):
        node = Node(key)

        if self.root == None:
            self.root = node
            return
        
        currentNode = self.root
        parentNode = None

        while currentNode is not None:
            parentNode = currentNode

            if key < currentNode.key:
                currentNode = currentNode.left
            elif key > currentNode.key:
                currentNode = currentNode.right
            else:
                return
            
        if key < parentNode.key:
            parentNode.left = node
        else:
            parentNode.right = node

    def search(self, key):
        
        currentNode = self.root

        while currentNode is not None:
            if currentNode.key == key:
                return True
            else:
                if key < currentNode.key:
                    currentNode = currentNode.left
                else:
                    currentNode = currentNode.right
        
        return False
    
    def remove(self, key):
        
        parentNode = None
        currentNode = self.root

        while currentNode is not None:
            if currentNode.key == key:
                if currentNode.left is None and currentNode.right is None:
                    if parentNode is not None:
                        if parentNode.left == currentNode:
                            parentNode.left = None
                        elif parentNode.right == currentNode:
                            parentNode.right = None
                    else:
                        self.root = None

                elif currentNode.left is not None and currentNode.right is not None:
                    biggestNodeParent = currentNode
                    biggestNode = currentNode.left

                    while biggestNode.right is not None:
                        biggestNodeParent = biggestNode
                        biggestNode = biggestNode.right
                    
                    currentNode.key = biggestNode.key

                    if biggestNodeParent.left == biggestNode:
                        biggestNodeParent.left = biggestNode.left
                    elif biggestNodeParent.right == biggestNode:
                        biggestNodeParent.right = biggestNode.left 

                else:
                    if currentNode.left is None:
                        childNode = currentNode.right
                    else:
                        childNode = currentNode.left
                    
                    if parentNode is not None:
                        if parentNode.right == currentNode:
                            parentNode.right = childNode
                        else:
                            parentNode.left = childNode
                    else:
                        self.root = childNode


            parentNode = currentNode

            if key < currentNode.key:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

        

    def preorder(self):
        string = ""

        if self.root == None:
            return
        
        currentNode = self.root
        memory = []
        latest = None
        
        while currentNode is not None or memory:

            while currentNode is not None:
                string += str(currentNode.key) + " "
                memory.append(currentNode)
                currentNode = currentNode.left

            for i in memory:
                latest = i
                
            memory.remove(latest)
            currentNode = latest
            currentNode = currentNode.right

        print(string)


if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    for key in keys:
        Tree.insert(key)

    Tree.preorder()         # 5 1 3 2 4 9 7 6
 
    print(Tree.search(6))   # True
    print(Tree.search(8))   # False
    
    Tree.remove(1)
    Tree.preorder()         # 5 3 2 4 9 7 6
    Tree.remove(9)
    Tree.preorder()         # 5 3 2 4 7 6 
    Tree.remove(3)
    Tree.preorder()         # 5 2 4 7 6