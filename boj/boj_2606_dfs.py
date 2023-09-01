n = int(input())  # 컴퓨터 수
graph = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(i):
    visited[i] = 1
    for ni in graph[i]:
        if visited[ni] == 0:
            dfs(ni)


visited = [0] * (n + 1)
dfs(1)
print(sum(visited) - 1)
