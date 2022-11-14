class Heap:
    def __init__(self):
        self.heap = [0]
    def printInternalArr(self):
        output = ""
        for item in self.heap:
            output += str(item) + " "
        print(output)
    def iterateUp(self, index):
        while index//2 > 0:
            if self.heap[index] < self.heap[index//2]:
                break
            temp = self.heap[index]
            self.heap[index] = self.heap[index//2]
            self.heap[index//2] = temp
            index = index//2
    def iterateDown(self, index):
        while index*2+1 < len(self.heap):
            nextIndex = index*2 if self.heap[index*2] > self.heap[index*2+1] else index*2+1
            if self.heap[index] > self.heap[nextIndex]:
                break
            temp = self.heap[index]
            self.heap[index] = self.heap[nextIndex]
            self.heap[nextIndex] = temp
            index = nextIndex

    def push(self, val):
        self.heap.append(val)
        self.iterateUp(len(self.heap)-1)
    def pop(self):
        if len(self.heap) <= 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop(len(self.heap)-1)
        ret = self.heap[1]
        self.heap[1] = self.heap.pop(len(self.heap)-1)
        self.iterateDown(1)
        return ret

heap = Heap()
heap.push(1)
heap.push(4)
heap.push(2)
heap.push(5)
heap.push(3)
heap.push(3)
heap.push(3)
heap.push(9)
heap.push(8)
heap.push(10)

print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
heap.push(100)
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
