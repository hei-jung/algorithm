import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

# graph = [[0] * N for _ in range(N)] # 인접 행렬
# for _ in range(M):
#     src, dst = map(int, sys.stdin.readline().split())
#     graph[src - 1][dst - 1] = graph[dst - 1][src - 1] = 1


graph = [[] for _ in range(N)]  # 인접 리스트
for _ in range(M):
    src, dst = map(int, sys.stdin.readline().split())
    graph[src - 1].append(dst - 1)
    graph[dst - 1].append(src - 1)

visited = []


# 깊이 우선 탐색
def dfs(src):
    # 방문 표시
    visited.append(src)
    # 시작 노드에 연결된 모든 노드 방문
    for i in sorted(graph[src - 1]):
        if i + 1 not in visited:
            dfs(i + 1)


dfs(V)
print(' '.join(list(map(str, visited))))

visited = []


# 너비 우선 탐색
def bfs(src):
    q = deque()
    q.append(src)  # 방문할 노드를 큐에 저장
    while q:
        i = q.popleft()  # 이번에 방문할 노드
        if i not in visited:
            visited.append(i)
        # print('이번에 방문할 노드', i, '에 연결된 노드들', graph[i - 1])
        for j in sorted(graph[i - 1]):  # i 노드에 연결된 노드들
            if j + 1 not in visited:  #
                q.append(j + 1)  # 다음에 방문할 노드로 지정
                visited.append(j + 1)


bfs(V)
print(' '.join(list(map(str, visited))))
