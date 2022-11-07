"""
question:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

using recursion to solve the problem
which give the right answer but is not efficient enough!!!
time: O(2^n)
mem: O(2^n)
"""
def climb(nStep):
    if nStep == 0:
        return 1
    elif nStep < 0:
        return 0
    return climb(nStep-1) + climb(nStep-2)

    
def climbStairs(n):
    return climb(n)

print(climbStairs(30))