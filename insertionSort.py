"""
Insertion sort
"""

def insertionSort(arr):
    sortedArr=[]
    for item in arr:
        if len(sortedArr) == 0:
            sortedArr.append(item)
            continue
        sortedArr = insert(sortedArr, item)

    return sortedArr

def insert(arr, e):
    i = len(arr)
    arr.append(e)
    while(i>1 and arr[i] < arr[i-1]):
        temp = arr[i-1]
        arr[i-1] = arr[i]
        arr[i] = temp
        i-=1
    return arr


arr = [1,2,2,6,3,5,1]
sortedArr = insertionSort(arr)
print(sortedArr)