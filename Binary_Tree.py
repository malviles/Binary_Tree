class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = None
        self.depth = None

    def insert_aux(self,Node, current):

        if Node.data < current.data:
            if current.left is None:
                current.left = Node
            else:    
                self.insert_aux(Node,current.left)
        else:
            if current.right is None:
                current.right = Node
            else:
                self.insert_aux(Node,current.right)
    
    def insert(self,Node):

        if self.root == None:
            self.root = Node
        else:
            self.insert_aux(Node,self.root)
    

    
    def check (self,current):
        if current == None:
            return print("None")
        if current.left:
            self.check(current.left)
        if current:
            print(current.data)
        if current.right:
            self.check(current.right)


class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None




n1 = Node(8)
n2= Node (12)
n3 = Node(1)
n4 = Node(2)
n5 = Node(10)


bt = BinaryTree()
bt.insert(n1)
bt.insert(n2)
bt.insert(n3)
bt.insert(n4)
bt.insert(n5)



bt.check(n1)