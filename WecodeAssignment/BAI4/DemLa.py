
class Node :
    def __init__(self,value) -> None:
        self.l = None
        self.r = None
        self.v = value

class Tree:
    def __init__(self) -> None:
        self.root = None

    
    def add(self,node,value):
        if self.root == None:
            self.root = Node(value)
        else:
            if value > node.v:
                if node.r == None:
                    node.r = Node(value)
                else:
                    self.add(node.r,value)
            elif value < node.v:
                if node.l == None:
                    node.l = Node(value)
                else:
                    self.add(node.l,value)

    def _countLeafNode(self,node):
        if node is None:
            return 0
        elif node.l is None and node.r is None :
            return 1
        else:
            return  self._countLeafNode(node.l) + self._countLeafNode(node.r)


tree =  Tree()

while True:
    n = int(input())
    if n!= 0:
        tree.add(tree.root,n)
    else:
        print(tree._countLeafNode(tree.root))
        break
 