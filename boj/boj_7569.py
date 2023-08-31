from collections import deque

m, n, h = map(int, input().split())  # m, n: 상자 크기 / h: 상자 수
dd = [-1, 1, 0, 0, 0, 0]  # 위, 아래
dy = [0, 0, -1, 1, 0, 0]  # 앞, 뒤
dx = [0, 0, 0, 0, -1, 1]  # 왼쪽, 오른쪽
graph = []
for i in range(h):
    graph.append([])
    for _ in range(n):
        graph[i].append(list(map(int, input().split())))


def bfs():
    global ans
    q = deque()
    visited = [[[-1] * m for _ in range(n)] for _ in range(h)]
    for d in range(h):
        for y in range(n):
            for x in range(m):
                if graph[d][y][x] == 1:
                    q.append((d, y, x))
                    visited[d][y][x] = 0
    while q:
        for _ in range(len(q)):
            d, y, x = q.popleft()
            for idx in range(6):
                nd = d + dd[idx]
                ny = y + dy[idx]
                nx = x + dx[idx]
                if nd < 0 or nd >= h or ny < 0 or ny >= n or nx < 0 or nx >= m:  # 범위 밖
                    continue
                if graph[nd][ny][nx] == -1 or graph[nd][ny][nx] == 1:  # 빈칸 or 이미 익은 토마토
                    continue
                if graph[nd][ny][nx] == 0 and visited[nd][ny][nx] == -1:
                    q.append((nd, ny, nx))
                    visited[nd][ny][nx] = visited[d][y][x] + 1
                    ans = max(ans, visited[nd][ny][nx])
    for d in range(h):
        for y in range(n):
            for x in range(m):
                if graph[d][y][x] == 0 and visited[d][y][x] == -1:
                    return False
    return True


ans = 0
if bfs():
    print(ans)
else:
    print(-1)
