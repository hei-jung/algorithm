from collections import deque

MAX = 100001


def bfs():
    q = deque([n])
    while q:
        x = q.popleft()
        for dx in (-1, 1, x):
            if 0 <= x + dx < MAX and visited[x + dx] == -1:
                q.append(x + dx)
                visited[x + dx] = visited[x] + 1


visited = [-1] * MAX
n, k = map(int, input().split())
visited[n] = 0
bfs()
print(visited[k])
