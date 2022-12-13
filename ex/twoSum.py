"""
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
"""

def twoSum (nums, target):
    visited = {}
    for i in range(len(nums)):
        r = target-nums[i]
        if r in visited:
            return [visited[r],r]
        visited[nums[i]] = i
    return None


s = twoSum([2,7,11,15], 9)
print(s)