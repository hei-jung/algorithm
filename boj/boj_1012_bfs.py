import sys
from collections import deque

input = sys.stdin.readline


def solution(graph):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    visited = [[0] * m for _ in range(n)]

    def bfs(y, x):
        q = deque([(y, x)])
        while q:
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1 and visited[ny][nx] == 0:
                    q.append((ny, nx))
                    visited[ny][nx] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                bfs(i, j)
    return cnt


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        m, n, k = map(int, input().split())
        graph = [[0] * m for _ in range(n)]
        for _ in range(k):
            x, y = map(int, input().split())
            graph[y][x] = 1
        answer = solution(graph)
        print(answer)
