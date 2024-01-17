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

    def postorder(self):
        currentNode = self.root
        string = ""
        memoryOfNodes= []
        memoryHelper = []
        memoryOfNodes.append(currentNode)

        while memoryOfNodes:

            for i in memoryOfNodes:
                latest = i
                
            memoryOfNodes.remove(latest)
            memoryHelper.append(latest)

            if latest.left is not None:
                memoryOfNodes.append(latest.left)
            if latest.right is not None:
                memoryOfNodes.append(latest.right)

        for z in reversed(memoryHelper):
            string += str(z.key) + " "
        
        print(string)
        #I got ideas of how to implement this method from this website (but I used lists instead of stack)https://www.tutorialspoint.com/binary-tree-postorder-traversal-in-python
        #Learned to use reversed method here https://www.programiz.com/python-programming/methods/built-in/reversed

    def inorder(self):
        currentNode = self.root
        string = ""
        memory = []

        while memory or currentNode:
            if currentNode is not None:
                memory.append(currentNode)
                currentNode = currentNode.left
            else:
                for i in memory:
                    latest = i
                    
                memory.remove(latest)
                currentNode = latest

                string += str(currentNode.key) + " "

                currentNode = currentNode.right
        
        print(string)

    def breadthfirst(self):
        string = ""
        currentNode = self.root
        order = []
        order.append(currentNode)

        while order:
            if order:
                first = order[0]

            order.remove(first)
            currentNode = first

            string += str(currentNode.key) + " "
            if currentNode.left:
                order.append(currentNode.left)
            if currentNode.right:
                order.append(currentNode.right)
        
        print(string)

if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    for key in keys:
        Tree.insert(key)
   
    Tree.postorder()        # 1 3 2 4 9 7 6 5
    Tree.inorder()          # 1 2 3 4 5 6 7 9
    Tree.breadthfirst()     # 5 1 9 3 7 2 4 6
