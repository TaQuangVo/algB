"""
binary search:
can only perform on a sorted array
time: O(logn)
mem: O(1)
"""

def binarySearch(arr, val, l, r):
    if r-l <= 0:
        return r if arr[r] == val else -1
    
    m = (r+l)//2
    if arr[m] > val:
        return binarySearch(arr, val, l, m-1)
    elif arr[m] < val:
        return binarySearch(arr, val, m+1, r)
    else:
        return m

def search(arr, val):
    return binarySearch(arr, val, 0, len(arr)-1)

arr = list(range(100))
print(search(arr, 31))