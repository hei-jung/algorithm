import sys

n = int(input())
game = []
for _ in range(n):
    game.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            break
        move = game[i][j]
        # 오른쪽으로 이동
        if j + move < n: dp[i][j + move] += dp[i][j]
        # 아래쪽으로 이동
        if i + move < n: dp[i + move][j] += dp[i][j]

print(dp[-1][-1])
