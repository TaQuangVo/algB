"""
Given a string s, find the length of the longest substring without repeating characters.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    visited = set()
    maxCount = 0

    i = 0
    j = 0
    while(j < len(s)):
        if s[j] not in visited:
            maxCount = max(j-i+1, maxCount)
            visited.add(s[j])
            j=j+1
        else:
            visited.remove(s[i])
            i=i+1

    return maxCount