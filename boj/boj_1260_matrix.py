import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = [[0] * N for _ in range(N)]  # 인접 행렬
for _ in range(M):
    src, dst = map(int, sys.stdin.readline().split())
    graph[src - 1][dst - 1] = graph[dst - 1][src - 1] = 1

visited = []


# 깊이 우선 탐색
def dfs(src):
    visited.append(src)
    for i in range(N):
        if graph[src - 1][i] and i + 1 not in visited:
            dfs(i + 1)


dfs(V)
print(' '.join(list(map(str, visited))))

visited = [V]


# 너비 우선 탐색
def bfs(src):
    q = deque()
    q.append(src)
    while q:
        i = q.popleft()
        for j in range(N):
            if graph[i - 1][j] and j + 1 not in visited:
                q.append(j + 1)
                visited.append(j + 1)


bfs(V)
print(' '.join(list(map(str, visited))))
