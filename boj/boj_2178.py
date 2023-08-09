from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(input()))))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우


def bfs(r, c):
    q = deque([(r, c)])
    visited = [[0] * m for _ in range(n)]  # 방문 좌표
    cnt = 1
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()  # 현재 위치 좌표
            if x == n - 1 and y == m - 1:
                return cnt
            for dx, dy in directions:
                if 0 <= x + dx < n and 0 <= y + dy < m and graph[x + dx][y + dy] == 1 and visited[x + dx][y + dy] != 1:
                    visited[x + dx][y + dy] = 1  # 방문 표시
                    q.append((x + dx, y + dy))  # 다음 번지 지정
        cnt += 1


ans = bfs(0, 0)  # 시작점 위치: (0, 0)
print(ans)
