from collections import deque

gears = []
for _ in range(4):
    # 총 8개의 톱니를 가지고 있는 톱니바퀴 4개
    # 12시 방향부터 시계방향 순서대로 / N극: 0, S극: 1
    gears.append(deque(map(int, list(input()))))


# 회전
def rotate(i, di):
    if di == 1:
        cog = gears[i].pop()
        gears[i].appendleft(cog)
    elif di == -1:
        cog = gears[i].popleft()
        gears[i].append(cog)


def dfs(i, di, r):
    if r[i] == 1:
        return
    r[i] = 1
    # 톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전하게 된다.
    # 맞닿은 부분이 서로 같으면 회전하지 않음.
    if i - 1 >= 0 and r[i - 1] != 1:
        if gears[i - 1][2] != gears[i][6]:
            dfs(i - 1, -di, r)
        else:
            dfs(i - 1, 0, r)
    if i + 1 < 4 and r[i + 1] != 1:
        if gears[i][2] != gears[i + 1][6]:
            dfs(i + 1, -di, r)
        else:
            dfs(i + 1, 0, r)
    rotate(i, di)


k = int(input())  # 회전 횟수
for _ in range(k):
    idx, d = map(int, input().split())  # d=1: 시계 방향 / d=-1: 반시계 방향
    visited = [0, 0, 0, 0]
    dfs(idx - 1, d, visited)

# [점수 계산]
score = 0
for x in range(4):
    if gears[x][0] == 1:
        score += 2 ** x
print(score)
