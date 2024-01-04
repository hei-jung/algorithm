import sys
import heapq

input = sys.stdin.readline

MAX = 401

n, m, k = map(int, input().split())
grid = []  # 격자 상태
is_shark = [[False] * n for _ in range(n)]  # 상어 존재 여부
for i in range(n):
    grid.append(list(map(int, input().split())))
    for j in range(n):
        if grid[i][j] > 0:
            is_shark[i][j] = True
direction = list(map(int, input().split()))
priority = [list(map(int, input().split())) for _ in range(m * 4)]
time = [[0] * n for _ in range(n)]  # 냄새 남은 시간

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def run():
    # 냄새 뿌리기
    for x in range(n):
        for y in range(n):
            if is_shark[x][y]:
                time[x][y] = k
            elif time[x][y] > 0:
                time[x][y] -= 1
                if time[x][y] == 0:
                    grid[x][y] = 0

    # 이동 방향 정하기
    tmp = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if is_shark[x][y]:  # 상어 있는 경우
                is_shark[x][y] = False
                s = grid[x][y] - 1  # 상어 번호
                d = direction[s] - 1  # s번 상어 현재 방향
                pq = []
                for i in range(4):  # s번 상어의 방향 우선순위
                    nd = priority[s * 4 + d][i]
                    nx = x + dx[nd - 1]
                    ny = y + dy[nd - 1]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if grid[nx][ny] == 0:  # 아무 냄새 없는 칸
                        heapq.heappush(pq, (i, nd))  # 순위, 방향
                    elif grid[nx][ny] == s + 1:
                        heapq.heappush(pq, (i + 4, nd))
                if pq:
                    _, nd = heapq.heappop(pq)
                    nx = x + dx[nd - 1]
                    ny = y + dy[nd - 1]
                    heapq.heappush(tmp[nx][ny], (s + 1, nd))  # 상어, 방향

    # 모든 상어 이동 후
    min_s = MAX
    true_cnt = 0
    for x in range(n):
        for y in range(n):
            if tmp[x][y]:
                is_shark[x][y] = True
                s, d = heapq.heappop(tmp[x][y])
                grid[x][y] = s
                direction[s - 1] = d
                min_s = min(min_s, s)
                true_cnt += 1

    if min_s == 1 and true_cnt == 1:
        return True
    else:
        return False


flag = False
for t in range(1, 1001):
    flag = run()
    if flag:
        break

print(t if flag else -1)
