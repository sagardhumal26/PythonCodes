class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
    def insert(self,data):
        if self.data:
            if (data < self.data):
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    
    def findval(self,val):
        if val < self.data:
            if self.left is None:
                return "val {} not present in Tree".format(val)
            return self.left.findval(val)
        elif val > self.data:
            if self.right is None:
                return "val {} not present in Tree".format(val)
            return self.right.findval(val)
        else:
            return "val {} present in Tree".format(val)
        
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()        

if __name__=='__main__':
    root=Node(10)
    root.insert(6)
    root.insert(14)
    root.insert(7)
    root.printTree()
    print(root.findval(7))
    print(root.findval(8))
