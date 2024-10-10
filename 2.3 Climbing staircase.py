def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    prev2, prev1 = 1, 2
    for i in range(3, n+1):
        prev2, prev1 = prev1, prev1 + prev2
    
    return prev1

n1 = 4
n2 = 3

print(climbStairs(n1))
print(climbStairs(n2))  
