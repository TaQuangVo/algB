"""
------ One Branch Recursion ------
factorial
f(n) = n * f(n-1)
f(1) = 1

Recursive
time: O(n)
mem: O(n)

Iterative
time: O(n)
mem: O(1)

computing factorial recursively is actually worse then just doit with a while loop
because the memory complexity will by O(1) instead.
"""

def facRe(a):
    if a <= 1:
        return a
    return a*facRe(a-1)

def facWh(a):
    re = 1
    while a >= 1:
        re *= a
        a-=1
    return re

a = 5
facReA = facRe(a)
facWhA = facWh(a)


print(facReA)
print(facWhA)


"""
------ Two Brand Recursion

fibonacci 
f(n) = f(n-1) + f(n-2)
f(1) = 1
f(0) = 0

Recursive
time: O(2^n)
mem: O(2^n)

Iterative
time: O(n)
mem: O(1)

"""

def fibRe(a):
    if a <= 1:
        return a
    return fibRe(a-1) + fibRe(a-2)

def fibWh(n):
    pre = 0
    cur = 1
    index = 1
    while index < n-1:
        temp = pre
        pre = cur
        cur += temp
        index += 1
    return pre + cur



a = 10
print(fibRe(a))
print(fibWh(a))
