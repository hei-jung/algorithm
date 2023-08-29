# N-Queen
# 퀸 N개를 서로 공격할 수 없게 놓는 방법의 수
# 퀸: 상하좌우 직선 / 대각선 이동 가능
n = int(input())
queen = [0] * n


def check(r):
    for i in range(r):
        if queen[r] == queen[i]:  # 같은 열
            return False
        if abs(r - i) == abs(queen[r] - queen[i]):  # 대각선
            return False
    return True


def dfs(r):
    global cnt
    if r == n:
        cnt += 1
        return
    for c in range(n):
        queen[r] = c
        if check(r):
            dfs(r + 1)  # 다음 행으로 이동


cnt = 0
dfs(0)
print(cnt)
