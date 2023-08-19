n = int(input())  # 전체 사람의 수
a, b = map(int, input().split())  # 촌수 계산할 두 사람
graph = [[] for _ in range(n + 1)]

m = int(input())  # 부모-자식 관계 수
for _ in range(m):
    x, y = map(int, input().split())  # x: 부모 / y: 자식
    graph[y].append(x)
    graph[x].append(y)

visited = [0] * (n + 1)


def dfs(i, depth):
    if i == b:
        print(depth)
        exit(0)
    for ni in graph[i]:
        if visited[ni] == 0:
            visited[ni] = 1
            dfs(ni, depth + 1)


visited[a] = 1
dfs(a, 0)
print(-1)
