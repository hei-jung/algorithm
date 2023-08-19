from collections import deque

f, s, g, u, d = map(int, input().split())
graph = [0] * (f + 1)
visited = [0] * (f + 1)


def bfs(i):
    q = deque([i])  # 현재 위치
    visited[i] = 1
    while q:
        i = q.popleft()
        if 0 < i + u <= f and visited[i + u] == 0:  # 올라갈 경우
            q.append(i + u)
            visited[i + u] = 1
            graph[i + u] = graph[i] + 1  # 경로 길이 +1
        if 0 < i - d <= f and visited[i - d] == 0:  # 내려갈 경우
            q.append(i - d)
            visited[i - d] = 1
            graph[i - d] = graph[i] + 1  # 경로 길이 +1


bfs(s)
ans = graph[g] if visited[g] == 1 else "use the stairs"
print(ans)
