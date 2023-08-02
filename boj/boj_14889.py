n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))

ans = 1000000000

visited = [0] * n  # 탐색 여부


def dfs(x, cnt):
    global ans
    if cnt == n // 2:
        start = 0
        link = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if visited[i] == 1 and visited[j] == 1:
                    start += s[i][j]
                    start += s[j][i]
                elif visited[i] == 0 and visited[j] == 0:
                    link += s[i][j]
                    link += s[j][i]
        ans = min(ans, abs(start - link))
        if ans == 0:
            print(0)
            exit(0)
        return
    for i in range(x, n):
        if visited[i] != 1:
            visited[i] = 1
            dfs(i + 1, cnt + 1)
            visited[i] = 0


dfs(0, 0)

print(ans)
