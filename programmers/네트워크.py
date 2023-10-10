def solution(n, computers):
    arr = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                arr[i].append(j)
    cnt = 0
    visited = [0] * n

    def dfs(i):
        visited[i] = 1
        for ni in arr[i]:
            if visited[ni] != 1:
                dfs(ni)

    for i in range(n):
        if visited[i] != 1:
            dfs(i)
            cnt += 1
    return cnt
