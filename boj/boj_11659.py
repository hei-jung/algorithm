import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# 구간 별 누적 합
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = dp[i - 1] + arr[i - 1]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(dp[j] - dp[i - 1])
