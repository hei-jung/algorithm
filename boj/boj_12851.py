from collections import deque

MAX = 100001


def bfs():
    cnt = 0
    q = deque([n])
    while q:
        x = q.popleft()
        if x == k:
            cnt += 1
            continue
        for dx in (-1, 1, x):
            nx = x + dx
            if 0 <= nx < MAX and (graph[nx] == -1 or graph[nx] == graph[x] + 1):
                q.append(nx)
                graph[nx] = graph[x] + 1
    return cnt


graph = [-1] * MAX
n, k = map(int, input().split())
graph[n] = 0
ans = bfs()
print(f"{graph[k]}\n{ans}")
