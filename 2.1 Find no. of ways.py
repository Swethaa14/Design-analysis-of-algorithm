def findPaths(m, n, N, i, j):
    result = 0
    dp = [[0] * n for _ in range(m)]
    dp[i][j] = 1

    for _ in range(N):
        new_dp = [[0] * n for _ in range(m)]
        for x in range(m):
            for y in range(n):
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        new_dp[nx][ny] += dp[x][y]
                    else:
                        result += dp[x][y]
        dp = new_dp

    return result

# Example usage:
print(findPaths(2, 2, 2, 0, 0))  # Output: 6
print(findPaths(1, 3, 3, 0, 1))  # Output: 12
