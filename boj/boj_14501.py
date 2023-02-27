import sys

# 구하고자 하는 것: 최대 이익
N = int(sys.stdin.readline())  # N+1: 퇴사일 (이 날부터는 회사에 없음)
T = [0] * N  # 상담을 완료하는데 걸리는 기간
P = [0] * N  # 상담을 했을 때 받을 수 있는 금액
dp = [0] * (N + 1)  # 최대 이익 저장

for i in range(N):
    T[i], P[i] = map(int, sys.stdin.readline().split())

for i in range(N - 1, -1, -1):
    if i + T[i] > N:  # 퇴사일부터는 상담 불가
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + T[i]] + P[i], dp[i + 1])

print(dp[0])
