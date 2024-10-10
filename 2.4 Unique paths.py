def uniquePaths(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]


m1, n1 = 7, 3
m2, n2 = 3, 2

print(uniquePaths(m1, n1))  
print(uniquePaths(m2, n2))  
