import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

dp = [1, 1]
for i in range(2, n + 1):
    dp.append(dp[i - 2] + dp[i - 1])

ans = 1
idx = 0  # 기준점 (고정석)
for _ in range(m):
    vip = int(sys.stdin.readline())
    ans *= dp[vip - idx - 1]  # 현재 고정석 왼쪽에 있는 좌석들의 자리 배치 경우의 수
    idx = vip
ans *= dp[n - idx]  # 마지막 고정석 오른쪽에 있는 좌석들의 자리 배치 경우의 수

print(ans)
