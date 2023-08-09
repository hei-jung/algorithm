n, m = map(int, input().split())  # 종이 크기
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
T = [
    [(0, -1), (0, 1), (1, 0)],  # ㅜ
    [(-1, 0), (1, 0), (0, -1)],  # ㅓ
    [(0, -1), (0, 1), (-1, 0)],  # ㅗ
    [(-1, 0), (1, 0), (0, 1)]  # ㅏ
]
visited = [[0] * m for _ in range(n)]  # 방문 표시
max_s = 0  # 최대 합


def dfs(x, y, cnt, s):
    global max_s
    if cnt == 4:  # 테트로미노 완성 시
        max_s = max(max_s, s)
        return
    for dx, dy in directions:
        if 0 <= x + dx < n and 0 <= y + dy < m and visited[x + dx][y + dy] != 1:
            visited[x + dx][y + dy] = 1
            dfs(x + dx, y + dy, cnt + 1, s + grid[x + dx][y + dy])
            visited[x + dx][y + dy] = 0


for i in range(n):
    for j in range(m):
        # T자 모양 테트로미노
        for directions_T in T:
            tmp = grid[i][j]
            for di, dj in directions_T:
                if 0 <= i + di < n and 0 <= j + dj < m:
                    tmp += grid[i + di][j + dj]
            max_s = max(max_s, tmp)
        # 그 외 모양 테트로미노
        visited[i][j] = 1
        dfs(i, j, 1, grid[i][j])
        visited[i][j] = 0

print(max_s)
