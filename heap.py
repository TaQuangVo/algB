class Heep:
    def __init__(self):
        self.arr = [0]
    def swap(self, i1, i2):
        temp = self.arr[i2]
        self.arr[i2] = self.arr[i1]
        self.arr[i1] = temp
    def iterateUp(self, index):
        pIndex = index // 2
        if self.arr[index] >= self.arr[pIndex]:
            return
        self.swap(index, pIndex)
        self.iterateUp(pIndex)
    def push(self, val):
        i = len(self.arr)
        self.arr.append(val)
        self.iterateUp(i)
    def iterateDown(self, index):
        minChildIndex = 0
        if index*2+1 <= len(self.arr)-1:
            minChildIndex = index*2 if self.arr[index*2] < self.arr[index*2+1] else index*2+1
        elif index*2 == len(self.arr)-1:
            minChildIndex = index*2
        if self.arr[index] < self.arr[minChildIndex] or minChildIndex == 0:
            return
        self.swap(index,minChildIndex)
        self.iterateDown(minChildIndex)
    def pop(self):
        if len(self.arr) <= 1:
            return None
        if len(self.arr) == 2:
            return self.arr.pop()
        ret = self.arr[1]
        self.arr[1] = self.arr.pop()
        self.iterateDown(1)
        return ret
        
heep = Heep()
heep.push(5)
heep.push(7)
heep.push(10)
heep.push(1)
heep.push(9)
heep.push(4)
heep.push(2)
heep.push(3)
heep.push(0)
heep.push(2)
heep.push(2)
heep.push(7)
print(heep.pop())
print(heep.pop())
print(heep.pop())
print(heep.pop())
print(heep.pop())
print(heep.pop())
print(heep.pop())
print(heep.pop())
print(heep.pop())
print(heep.pop())
print(heep.pop())
print(heep.pop())

