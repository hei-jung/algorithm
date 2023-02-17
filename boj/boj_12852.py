import sys

n = int(sys.stdin.readline())

dp = [0] * (n + 1)  # 연산 횟수를 저장
path = ["" for _ in range(n + 1)]
path[1] = "1"

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1  # 빼기 1
    num = i - 1

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:  # 나누기 2
        dp[i] = dp[i // 2] + 1
        num = i // 2

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:  # 나누기 3
        dp[i] = dp[i // 3] + 1
        num = i // 3

    path[i] += str(i) + " " + path[num]

print(dp[n])
print(path[n])
