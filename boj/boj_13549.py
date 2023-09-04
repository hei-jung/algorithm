from collections import deque

MAX = 100001


def bfs():
    q = deque([n])
    visited[n] = 0
    while q:
        x = q.popleft()
        if x == k:
            return
        if 0 < 2 * x < MAX and visited[2 * x] == -1:
            q.appendleft(2 * x)  # 우선순위
            visited[2 * x] = visited[x]
        if 0 <= x - 1 < MAX and visited[x - 1] == -1:
            q.append(x - 1)
            visited[x - 1] = visited[x] + 1
        if 0 <= x + 1 < MAX and visited[x + 1] == -1:
            q.append(x + 1)
            visited[x + 1] = visited[x] + 1


visited = [-1] * MAX
n, k = map(int, input().split())
bfs()
print(visited[k])
