import sys

n, m = map(int, sys.stdin.readline().split())
dp = []
for _ in range(n):
    dp.append(list(map(int, sys.stdin.readline().split())))

# 첫 행
for c in range(1, m):
    dp[0][c] += dp[0][c - 1]

# 첫 열
for r in range(1, n):
    dp[r][0] += dp[r - 1][0]

# 두 번째 열부터
for r in range(1, n):
    for c in range(1, m):
        dp[r][c] += max(dp[r][c - 1], dp[r - 1][c - 1], dp[r - 1][c])

print(dp[n - 1][m - 1])
