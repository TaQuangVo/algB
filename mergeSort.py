"""
mergeSort
No. layers of recurtion: log(n)
time complexity of each layer: O(n)

time: O(nlogn)
mem: O(n)

merge short can be stable.
"""

def merge(arr, s, m, e):
    leftHalf = arr[s:m+1]
    rightHalf = arr[m+1:e+1]
    leftI = 0
    rightI = 0

    while leftI < len(leftHalf) or rightI < len(rightHalf):
        index = s + leftI + rightI
        if leftI >= len(leftHalf):
            arr[index] = rightHalf[rightI]
            rightI += 1
            continue
        elif rightI >= len(rightHalf):
            arr[index] = leftHalf[leftI]
            leftI += 1
            continue
        if leftHalf[leftI] < rightHalf[rightI]:
            arr[index] = leftHalf[leftI]
            leftI += 1
            continue
        arr[index] = rightHalf[rightI]
        rightI += 1



def mergeSort(arr, s, e):
    if (e-s) == 0:
        return
    m = (e+s)//2

    mergeSort(arr, s, m)
    mergeSort(arr, m+1, e)

    merge(arr, s, m , e)

    return arr


arr = [1,9,2,6,3,5,14,7,1,2]
sortedArr = mergeSort(arr, 0, len(arr)-1)
print(sortedArr)
