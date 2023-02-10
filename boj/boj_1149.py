import sys

n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, sys.stdin.readline().split())))

r, g, b = 0, 1, 2
for i in range(1, n):
    dp[i][r] += dp[i - 1][g] if dp[i - 1][b] > dp[i - 1][g] else dp[i - 1][b]
    dp[i][g] += dp[i - 1][r] if dp[i - 1][b] > dp[i - 1][r] else dp[i - 1][b]
    dp[i][b] += dp[i - 1][r] if dp[i - 1][g] > dp[i - 1][r] else dp[i - 1][g]

print(min(dp[-1]))
