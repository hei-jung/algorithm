import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

dp = [10001] * (k + 1)  # 10001 = 최대 동전 갯수 + 1
dp[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k]) if dp[k] != 10001 else print(-1)
