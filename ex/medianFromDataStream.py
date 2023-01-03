class Heap(object):
    def __init__(self, _type=1):
        if _type != 1 and _type != -1:
            print("invalid type: " + str( _type ))
            return None
        self.arr = [0]
        self.type = _type

    def swap(self, i1, i2):
        temp = self.arr[i1]
        self.arr[i1] = self.arr[i2]
        self.arr[i2] = temp

    def iterate_up(self, i):
        pi = i // 2
        if pi <= 0 or self.arr[i] <= self.arr[pi]:
            return
        self.swap(i, pi)
        self.iterate_up(pi)

    def iterate_down(self, i):
        li = i*2
        ri = i*2+1
        if li >= len(self.arr):
            return
        largest_child_i = li
        if li != len(self.arr)-1:
            largest_child_i = li if self.arr[li] > self.arr[ri] else ri
        if self.arr[i] < self.arr[largest_child_i]:
            self.swap(i, largest_child_i)
            self.iterate_down(largest_child_i)

    def push(self, val):
        self.arr.append(val*self.type)
        self.iterate_up(len(self.arr)-1)
    
    def pop(self):
        if len(self.arr) == 1:
            return None
        if len(self.arr) == 2:
            return self.arr.pop() * self.type
        ret_val = self.arr[1] * self.type
        self.arr[1] = self.arr.pop()
        self.iterate_down(1)
        return ret_val
    
    def peek(self):
        if len(self.arr) == 1:
            return None
        return self.arr[1] * self.type
    
    def len(self):
        return len(self.arr)-1



class MedianFinder(object):

    def __init__(self):
        self.min_heap = Heap(-1)
        self.max_heap = Heap(1)

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.max_heap.peek() > num:
            self.max_heap.push(num)
        else:
            self.min_heap.push(num)
        
        if self.max_heap.len() > self.min_heap.len()+1:
            self.min_heap.push(self.max_heap.pop())
        if self.min_heap.len() > self.max_heap.len()+1:
            self.max_heap.push(self.min_heap.pop())

    def findMedian(self):
        """
        :rtype: float
        """
        if self.max_heap.len() == self.min_heap.len():
            return float(self.max_heap.peek() + self.min_heap.peek()) / 2.0
        if self.min_heap.len() > self.max_heap.len():
            return self.min_heap.peek()
        if self.max_heap.len() > self.min_heap.len():
            return self.max_heap.peek()
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
