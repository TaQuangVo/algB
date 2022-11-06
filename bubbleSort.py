"""
bubble sort
time: O(n^2)
mem: O(1)
"""

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr = swap(arr, j, j+1)
    return arr

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr


arr = [1,2,2,6,3,5,1]
sortedArr = bubbleSort(arr)
print(sortedArr)