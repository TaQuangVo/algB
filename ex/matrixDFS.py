"""
    find the total number of path from (0,0) to (r,c)
"""

def backtracking(arr, r, c, visit):
    if  min(r,c) < 0:
        return 0
    if r >= len(arr) or c >= len(arr[0]):
        return 0
    if (r, c) in visit:
        return 0
    if arr[r][c] == 1:
        return 0
    if r == len(arr)-1 or c == len(arr[0]):
        return 1
    
    visit.add((r,c))
    count = backtracking(arr, r-1, c, visit)
    count = count + backtracking(arr, r+1, c, visit)
    count = count + backtracking(arr, r, c-1, visit)
    count = count + backtracking(arr, r, c+1, visit)
    visit.remove((r,c))

    return count

arr = [
    [0,0,1,1,1],
    [1,0,0,1,0],
    [1,1,0,0,1],
    [1,0,0,0,0]
]
noPath = backtracking(arr, 0, 0, set())
print(noPath)


