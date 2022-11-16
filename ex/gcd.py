"""
    Euklides alg to find GCD
"""

def gcd(a, b):
    r = max(a,b)%min(a,b)
    if r == 0:
        return min(a,b)
    return gcd(min(a,b), r)

d = gcd(19, 42)
print(d)
