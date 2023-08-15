import sys
from collections import deque

sys.setrecursionlimit(10000)  # DFS 재귀 에러 방지

directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]  # 걸어갈 수 있는 방향


def dfs(x, y):
    for dx, dy in directions:
        if 0 <= x + dx < h and 0 <= y + dy < w and graph[x + dx][y + dy] == 1:
            graph[x + dx][y + dy] = -1  # 방문 표시
            dfs(x + dx, y + dy)


def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            if 0 <= x + dx < h and 0 <= y + dy < w and graph[x + dx][y + dy] == 1:
                graph[x + dx][y + dy] = -1  # 방문 표시
                q.append((x + dx, y + dy))


while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))  # 1은 땅, 0은 바다

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                graph[i][j] = -1
                # dfs(i, j)
                bfs(i, j)
                cnt += 1

    print(cnt)
