import sys

MAX = 1000000

dp = [1, 1, 2]
for i in range(3, MAX + 1):
    dp.append((dp[i - 3] + dp[i - 2] + dp[i - 1]) % 1000000009)

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    print(dp[n])
