"""
given an array, return if there are 2 elevents within 
a window of size k that are equal.
[1,2,4,1,6,5,1,3] , 3 -> true
"""
def findDouble(arr, k):
    window = set()
    l = 0
    r = 0
    while r < len(arr):
        print(window)
        if arr[r] in window:
            return True
        window.add(arr[r])

        r = r+1
        if r>k-1:
            window.remove(arr[l])
            l = l+1
    return False

arr = [1,2,4,2,6,5,1,3]
found = findDouble(arr, 3)
print(found)