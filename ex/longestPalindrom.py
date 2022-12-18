
    
def is_palindrom(s, start, end):
    return s[int(start)] == s[int(end)]

def check_palindrom_at( s, i):
    l = i
    r = i

    if i%1 != 0:
        l = l-0.5
        r = r+0.5

    while(is_palindrom(s,l,r)):
        l = l-1
        r = r+1
        if l < 0 or r >= len(s):
            break

    return (l+1,r-1)

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    longest = (0,0)
    for i in range(0, len(s)*2-1):
        temp = check_palindrom_at(s, (float)(i)/2)
        if temp[1]-temp[0] >= longest[1]-longest[0]:
            longest = temp
    return s[int(longest[0]):int(longest[1])+1]


def longestPalindrome_d(s):
    mem = [[False for col in range(len(s))] for row in range(len(s))]
    
    max_s = (0,0)
    no = 1

    for i in range(len(s)):
        mem[i][i] = True

    while (no < len(s)):
        l = 0
        while (l + no < len(s)):
            r = l+no
            mem[l][r] = (s[l] == s[r] and (mem[l+1][r-1] or r-l <= 2))
            print(s[l:r+1])
            if(r-l >= max_s[1] - max_s[0] and mem[l][r]):
                max_s = (l,r)
            l = l + 1
        no = no + 1
        l = 0

    return s[max_s[0]: max_s[1]+1]


s = "a00aa"
p = longestPalindrome_d(s)
print(p)