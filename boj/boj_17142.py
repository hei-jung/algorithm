from collections import deque
from itertools import combinations

n, m = map(int, input().split())
grid = []  # 연구소 상태:- 0: 빈 칸, 1: 벽, 2: 비활성 바이러스
for _ in range(n):
    grid.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

MAX = 999999


def infection(arr):  # 빈 칸에 퍼뜨려
    t = 0  # 복제 시간
    q = deque(arr)
    visited = [[-1] * n for _ in range(n)]
    for x, y in arr:
        q.append((x, y))
        visited[x][y] = 0
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if grid[nx][ny] == 0 and visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    t = max(t, visited[nx][ny])
                elif grid[nx][ny] == 2 and visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0 and visited[i][j] == -1:  # 빈 칸인데 방문 안 했을 경우
                return -1
    return t


virus = []
for r in range(n):
    for c in range(n):
        if grid[r][c] == 2:
            virus.append((r, c))
ans = MAX
for active in combinations(virus, m):
    time = infection(list(active))
    if time != -1:
        ans = min(ans, time)
print(ans if ans != MAX else -1)
