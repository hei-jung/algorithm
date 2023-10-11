def dfs(depth):
    global max_s
    if depth == 11:
        s = 0
        for stat in visited:
            s += stat
        max_s = max(max_s, s)
        return
    for pos in range(11):
        if graph[depth][pos] != 0 and visited[pos] == 0:
            visited[pos] = graph[depth][pos]
            dfs(depth + 1)
            visited[pos] = 0


if __name__ == '__main__':
    C = int(input())
    for _ in range(C):
        graph = []
        for _ in range(11):
            graph.append(list(map(int, input().split())))
        visited = [0] * 11
        max_s = 0
        dfs(0)
        print(max_s)
