import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

dp = [0] * (k + 1)
dp[0] = 1  # 0으로 만드는 방법 1가지 (동전 하나도 안 씀)

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]

print(dp[k])
