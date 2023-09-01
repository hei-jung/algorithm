from collections import deque

n = int(input())  # 컴퓨터 수
graph = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs():
    global cnt
    q = deque([1])
    visited = [0] * (n + 1)
    visited[1] = 1
    while q:
        i = q.popleft()
        for ni in graph[i]:
            if visited[ni] != 1:
                q.append(ni)
                visited[ni] = 1
        cnt += 1


cnt = -1
bfs()
print(cnt)
