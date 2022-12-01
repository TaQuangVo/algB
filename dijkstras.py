class Heap:
    def __init__(self):
        self.arr = [("0",0)]
    def swap(self, i1, i2):
        temp = self.arr[i2]
        self.arr[i2] = self.arr[i1]
        self.arr[i1] = temp
    def iterateUp(self, index):
        pIndex = index // 2
        if self.arr[index][1] >= self.arr[pIndex][1]:
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
            minChildIndex = index*2 if self.arr[index*2][1] < self.arr[index*2+1][1] else index*2+1
        elif index*2 == len(self.arr)-1:
            minChildIndex = index*2
        if self.arr[index][1] < self.arr[minChildIndex][1] or minChildIndex == 0:
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
    def length(self):
        return len(self.arr)-1

def build_adjacency_list(edges):
    adj_list = {}
    for i in range(len(edges)):
        if edges[i][0] not in adj_list:
            adj_list[edges[i][0]] = []
        if edges[i][1] not in adj_list:
            adj_list[edges[i][1]] = []
        adj_list[edges[i][0]].append((edges[i][1],edges[i][2]))
    return adj_list

def dijkstras(adj_graph, src, end): 
    min_cost = {}
    heap = Heap()
    heap.push((src,0))
    while heap.length() > 0:
        n,w = heap.pop()
        if n in min_cost:
            continue
        min_cost[n] = w
        print(n)
        for n1,w1 in adj_graph[n]:
            if n1 in min_cost:
                continue
            heap.push((n1,w+w1))
    return min_cost
        


#define edges --- (from, to, weight)
edges = [
    ("a","b",10),
    ("a","c",3),
    ("b","d",2),
    ("c","b",4),
    ("c","d",8),
    ("c","e",2),
    ("d","f",3),
    ("e","d",1),
    ("e","f",7),
    
]
adj_graph = build_adjacency_list(edges)
min_const_list = dijkstras(adj_graph,"a","d")
print(adj_graph)
print(min_const_list)
