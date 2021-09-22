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



    def BFS(self):
        expand = [self.root]
        #result = []
        while len(expand):
            #result.append(expand[0].v)
            print(str(expand[0].v), end= " ")
            if expand[0].l != None:
                expand.append(expand[0].l)
            if expand[0].r != None:
                expand.append(expand[0].r)
            expand.pop(0)
        #return result

tree =  Tree()
#x = [393,981,841,133,891,739,663,119,865,54,631,561,51,227,841,352,996,505]

while True:
    n = int(input())
    if n!= 0:
    #for n in x:
        tree.add(tree.root,n)
    else:
        tree.BFS()
        break
    

