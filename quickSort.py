"""
quick sort
No. layers of recursion: log(n)
time complexity of each layer: O(n)

time: O(nlogn)
mem: O(1)
"""


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partition(arr,s, e):
    j = s-1
    i = s
    while i < e:
        if(arr[i] <= arr[e]):
            j += 1
            swap(arr,i, j)
        i += 1
    j += 1
    swap(arr, j, e)
    return j


def quickSort(arr, s, e):
    if(e-s) <= 0:
        return

    m = partition(arr,s, e)

    quickSort(arr, s, m-1)
    quickSort(arr, m+1, e)

    return arr



arr = [9,2,6,1,5,3,7,0,8,6]
sortedArr = quickSort(arr, 0, len(arr)-1)
print(sortedArr)