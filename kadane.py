"""
return the max sum of a sub array, given an array.
[-2,3,3,-1,1,-6,3] -> 5
"""

def kadane(arr):
    gMax = arr[0]
    lMax = arr[0]

    for i in range(1, len(arr)):
        if lMax + arr[i] < arr[i]:
            lMax = arr[i]
        else:
            lMax = lMax + arr[i]
        if lMax > gMax:
            gMax = lMax
    return gMax


arr = [-2,3,-3,1,1,-6,3]
sum = kadane(arr)
print(sum)