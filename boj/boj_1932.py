import sys

n = int(sys.stdin.readline())

dp = []
for _ in range(n):
    dp.append(list(map(int, sys.stdin.readline().split())))

for i in range(n - 2, -1, -1):
    for j in range(i + 1):
        dp[i][j] += dp[i + 1][j] if dp[i][j] + dp[i + 1][j] > dp[i][j] + dp[i + 1][j + 1] else dp[i + 1][j + 1]

print(dp[0][0])
