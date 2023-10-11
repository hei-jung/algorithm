from collections import deque


def solution(n, computers):
    arr = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                arr[i].append(j)
    cnt = 0
    visited = [0] * n

    def bfs(i):
        q = deque([i])
        while q:
            i = q.popleft()
            for ni in arr[i]:
                if visited[ni] != 1:
                    q.append(ni)
                    visited[ni] = 1

    for i in range(n):
        if visited[i] != 1:
            bfs(i)
            cnt += 1
    return cnt
