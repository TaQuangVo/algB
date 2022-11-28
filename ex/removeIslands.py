"""
given an array, remove all 1s that not connected to border
[[0,0,1,0,1,0],
 [1,0,1,0,0,0],
 [1,1,0,1,1,0],
 [1,0,1,1,0,1],
 [1,1,0,0,1,0]]
"""

def printArr(arr):
    for r in range(len(arr)):
        strr = ""
        for c in range(len(arr[0])):
            strr = strr + ""+ str(arr[r][c]) + " "
        print(strr)

def mark_land(arr, r, c):
    if r < 0 or c < 0 or r >= len(arr) or c >= len(arr[0]):
        return
    if arr[r][c] != 1:
        return
    arr[r][c] = 2
    mark_land(arr, r+1, c)
    mark_land(arr, r, c+1)
    mark_land(arr, r-1, c)
    mark_land(arr, r, c-1)


def remove_islands(arr):
    #mark land vertical
    for i in range(len(arr)):
        mark_land(arr, i, 0)
        mark_land(arr, i, len(arr[0])-1)
    #mark land horizontal
    for i in range(len(arr[0])):
        mark_land(arr, 0, i)
        mark_land(arr, len(arr)-1, i)
    #remove island
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c] == 0:
                continue
            arr[r][c] = arr[r][c] - 1

    return arr

arr =  [[0,0,0,0,1,0],
        [1,0,1,0,0,0],
        [1,1,0,1,1,0],
        [1,0,1,1,0,1],
        [1,1,0,0,1,0]]

res = remove_islands(arr)
printArr(res)