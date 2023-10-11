from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    q = deque([(0, 0)])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    cnt = 0
    while q:
        for _ in range(len(q)):
            y, x = q.popleft()
            if y == n - 1 and x == m - 1:
                return cnt + 1
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= m or maps[ny][nx] == 0 or visited[ny][nx] == 1:
                    continue
                q.append((ny, nx))
                visited[ny][nx] = 1
        cnt += 1
    return -1
