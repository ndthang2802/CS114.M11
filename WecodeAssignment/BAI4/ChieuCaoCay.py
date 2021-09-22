import sys
from collections import deque
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

    def _height(self,node):
        if node == None:
            return 0
        else:
            left_height = 0
            right_height = 0
            if node.l != None:
                left_height =  self._height(node.l)
            if node.r != None:
                right_height = self._height(node.r)
            return max(left_height,right_height) + 1

tree =  Tree()
x = deque()
while True:
    n = list(map(int,sys.stdin.readline().split()))
    if n[0] == 0:
        x.insert(0,n[1])
    elif n[0] == 1:
        x.append(n[1])
    elif n[0] == 2:
        try :
            i = x.index(n[1])
            x.insert(i+1,n[2])
        except:
            x.insert(0,n[2])
    else:
        break
for i in x:
    tree.add(tree.root,i)
    
print(tree._height(tree.root))
