import math

class Queue:
    def __init__(self):
        self.q = []
    def enqueue(self, val):
        self.q.append(val)
    def dequeue(self):
        if len(self.q) == 0:
            return None
        return self.q.pop(0)
    def length(self):
        return len(self.q)
    def view(self):
        q = ""
        for item in self.q:
            q = q+ str(item)+ " "
        print(q)

class Tree:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
    def add(self, val):
        if self.val is None:
            self.val = val
            return val
        elif self.val > val:
            if self.left is None:
                self.left = Tree()
            return self.left.add(val)
        elif self.val < val:
            if self.right is None:
                self.right = Tree()
            return self.right.add(val)
        return None
    def addAll(self, vals):
        for val in vals:
            self.add(val)
    def find(self, val):
        if self.val == val:
            return val
        elif self.val == None:
            return None
        elif self.val < val and self.right is not None:
            return self.right.find(val)
        elif self.val > val and self.left is not None:
            return self.left.find(val)
        return None
    def findMin(self):
        if self.val == None:
            return None
        elif self.left is not None:
            return self.left.findMin()
        return self.val
    def findMax(self):
        if self.val == None:
            return None
        elif self.right is not None:
            return self.right.findMax()
        return self.val
    def remove(self, val):
        if self.val < val:
            self.right = self.right.remove(val)
            return self
        elif self.val > val:
            self.left = self.left.remove(val)
            return self
        elif self.val == val:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min = self.right.findMin()
                self.val = min 
                self.right = self.right.remove(min)
                return self
                
    def traverse(self):
        q = Queue()
        if self.val is not None:
            q.enqueue(self)
        nrOfLayers = 0
        while q.length() > 0:
            nrOfLayers += 1
            vals = ""
            for i in range(q.length()):
                node = q.dequeue()
                vals += str(node.val) + " "
                if node.left is not None:
                    q.enqueue(node.left)
                if node.right is not None:
                    q.enqueue(node.right)
            print(vals)
    def viewStructure(self):
        isLayerEmpty = True
        nrOfLayers = 0
        q = Queue()

        if self.val is not None:
            q.enqueue(self)
            isLayerEmpty = False
            nrOfLayers += 1
        if not isLayerEmpty:
            while not isLayerEmpty:
                vals = ""
                isLayerEmpty = True
                for i in range(q.length()):
                    node = q.dequeue()
                    if node is None:
                        vals += "_" + " "
                        q.enqueue(None)
                        q.enqueue(None)
                        continue
                    else:
                        vals += str(node.val) + " "

                    if node.left is not None:
                        q.enqueue(node.left)
                        isLayerEmpty = False
                    else:
                        q.enqueue(None)
                    if node.right is not None:
                        q.enqueue(node.right)
                        isLayerEmpty = False
                    else:
                        q.enqueue(None)
                nrOfLayers += 1
                print(vals)
                

        
tree = Tree()
tree.addAll([5,3,2,4,8,7,9,-1,-3, 11, 14])
tree.viewStructure()
tree.remove(5)
tree.viewStructure()





