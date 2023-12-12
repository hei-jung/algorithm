from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 빙산 녹는 과정
def melt(x, y):
    ocean_cnt = 0  # 접해있는 바다
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # graph[nx][ny] == 0 && visited[nx][ny] == 1: 빙산
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and visited[nx][ny] == 0:
            ocean_cnt += 1
    return max(0, graph[x][y] - ocean_cnt)


# 덩어리 개수
def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 0 and visited[nx][ny] != 1:
                q.append((nx, ny))
                visited[nx][ny] = 1


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ans = 0  # 시간
while 1:
    # 빙산 덩어리 개수
    cnt = 0
    visited = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if graph[r][c] != 0 and visited[r][c] != 1:
                cnt += 1
                bfs(r, c)
    if cnt > 1:  # 2 덩어리 이상으로 분리
        print(ans)
        break
    # 빙산 녹기
    flag = True
    ans += 1
    visited = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if graph[r][c] != 0:  # 빙산인 경우
                flag = False
                visited[r][c] = 1
                graph[r][c] = melt(r, c)
    if flag:  # 빙산이 다 녹음
        print(0)
        break
