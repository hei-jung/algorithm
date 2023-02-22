import sys

T = int(sys.stdin.readline())

dp = [0] * 42
dp[0] = 1
dp[1] = 0
dp[2] = 1

for i in range(3, 42):
    dp[i] = dp[i - 2] + dp[i - 1]

for _ in range(T):
    N = int(sys.stdin.readline())
    print(dp[N], dp[N + 1])
