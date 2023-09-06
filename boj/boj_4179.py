from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check(arr):
    print()
    for x in range(r):
        for y in range(c):
            print(arr[x][y], end=' ')
        print()


def f_bfs(q):
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= r or ny < 0 or ny >= c or graph[nx][ny] == '#':
                continue
            if f_visited[nx][ny] == -1:
                q.append((nx, ny))
                f_visited[nx][ny] = f_visited[x][y] + 1


def j_bfs(q):
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                return x, y
            if graph[nx][ny] == '#' or j_visited[nx][ny] >= 0:
                continue
            if f_visited[nx][ny] != -1 and f_visited[nx][ny] <= j_visited[x][y] + 1:
                continue
            q.append((nx, ny))
            j_visited[nx][ny] = j_visited[x][y] + 1
    return -1, -1


r, c = map(int, input().split())
graph = []
si, sj = r - 1, c - 1
for _ in range(r):
    graph.append(list(input()))
f_visited = [[-1] * c for _ in range(r)]
j_visited = [[-1] * c for _ in range(r)]
fq = deque()
jq = deque()
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            jq.append((i, j))
            j_visited[i][j] = 0
        elif graph[i][j] == 'F':
            fq.append((i, j))
            f_visited[i][j] = 0
f_bfs(fq)
i, j = j_bfs(jq)
if i == -1 and j == -1:
    print("IMPOSSIBLE")
else:
    print(j_visited[i][j] + 1)
