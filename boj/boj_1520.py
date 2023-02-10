import sys

m, n = map(int, sys.stdin.readline().split())
arr = []
for _ in range(m):
    arr.append(list(map(int, sys.stdin.readline().split())))

dp = [[-1] * n for _ in range(m)]


def dfs(i, j):
    if i == m - 1 and j == n - 1: return 1

    if dp[i][j] != -1: return dp[i][j]

    dp[i][j] = 0

    if i - 1 >= 0 and arr[i][j] > arr[i - 1][j]: dp[i][j] += dfs(i - 1, j)
    if i + 1 < m and arr[i][j] > arr[i + 1][j]: dp[i][j] += dfs(i + 1, j)
    if j - 1 >= 0 and arr[i][j] > arr[i][j - 1]: dp[i][j] += dfs(i, j - 1)
    if j + 1 < n and arr[i][j] > arr[i][j + 1]: dp[i][j] += dfs(i, j + 1)

    return dp[i][j]


print(dfs(0, 0))
