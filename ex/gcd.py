def gcd(a, b):
    r = max(a,b)%min(a,b)
    if r == 0:
        return min(a,b)
    return gcd(b, r)

d = gcd(3392, 356)
print(d)
