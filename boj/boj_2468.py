# 물에 잠기지 않는 영역: 물에 잠기지 않는 지점들이 상하좌우 인접 / 그 크기가 최대.
import sys

sys.setrecursionlimit(100000)

n = int(input())  # 2 이상 100 이하
graph = []
max_h = 1
for i in range(n):
    graph.append(list(map(int, input().split())))
    max_h = max(max_h, max(graph[i]))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(x, y, r):
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > r and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny, r)


ans = 1  # 아무 지역도 물에 잠기지 않을 경우 => 안전 영역 크기: 1
for h in range(1, max_h + 1):  # 내리는 비의 양에 따른 모든 경우 다 조사
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and visited[i][j] == 0:
                visited[i][j] = 1
                dfs(i, j, h)
                cnt += 1
    ans = cnt if ans < cnt else ans

print(ans)
