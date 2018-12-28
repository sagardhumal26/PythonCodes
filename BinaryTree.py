from asyncio.queues import Queue
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
    def insert(self,data):
        if self.data:
            if (data < self.data):
                if self.left is None:
                    print("Left is None")
                    self.left=Node(data)
                else:
                    print("Adding to Left")
                    self.left.insert(data)
            else:
                if self.right is None:
                    print("Right is None")
                    self.right=Node(data)
                else:
                    print("Adding to Right")
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
        
    def maxDepth(self):
        if self is None:
            return 0
        else:
            ldepth=rdepth=0
            if self.left:
                ldepth = self.left.maxDepth()
            if self.right:
                rdepth = self.right.maxDepth()
            return ldepth+1 if ldepth > rdepth else rdepth+1
    
    def DFS_preOrder(self):
        if self:
            print(self.data,end="->")
        if self.left:
            self.left.DFS_preOrder()
        if self.right:
            self.right.DFS_preOrder()
            
    def DFS_inOrder(self):
        if self.left:
            self.left.DFS_inOrder()
        if self:
            print(self.data,end="->")
        if self.right:
            self.right.DFS_inOrder()
            
    def DFS_postOrder(self):
        if self.left:
            self.left.DFS_postOrder()
        if self.right:
            self.right.DFS_postOrder()
        if self:
            print(self.data,end="->")
                
    def BFS(self):
        pass
                
    def deleteNode(self):
        pass

if __name__=='__main__':
    root=Node(10)
    root.insert(6)
    root.insert(14)
    root.insert(7)
    root.printTree()
    print(root.findval(7))
    print(root.findval(8))
    print(root.maxDepth())
    root.DFS_preOrder()
    print()
    root.DFS_inOrder()
    print()
    root.DFS_postOrder()
    print()
    root.BFS()
