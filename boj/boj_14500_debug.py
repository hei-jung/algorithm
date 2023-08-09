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


def dfs(x, y, cnt, visited_arr):
    global max_s
    if cnt == 4:  # 테트로미노 완성 시
        for r in range(n):
            for c in range(m):
                print(visited[r][c], end='')
            print()
        print()
        s = 0
        for r, c in visited_arr:
            s += grid[r][c]
        max_s = max(max_s, s)
        return
    for dx, dy in directions:
        if 0 <= x + dx < n and 0 <= y + dy < m and visited[x + dx][y + dy] != 1:
            visited[x + dx][y + dy] = 1
            visited_arr.append((x + dx, y + dy))
            dfs(x + dx, y + dy, cnt + 1, visited_arr)
            visited[x + dx][y + dy] = 0
            visited_arr.pop()


for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        # T자 모양 테트로미노
        for directions_T in T:
            tmp = grid[i][j]
            is_out = False
            for di, dj in directions_T:
                if 0 <= i + di < n and 0 <= j + dj < m:
                    tmp += grid[i + di][j + dj]
                    visited[i + di][j + dj] = 1
                else:
                    is_out = True
            max_s = max(max_s, tmp)
            if is_out:
                for r in range(n):
                    for c in range(m):
                        visited[r][c] = 0
            if not is_out:
                for r in range(n):
                    for c in range(m):
                        print(visited[r][c], end='')
                        visited[r][c] = 0
                    print()
                print()
        # 그 외 모양 테트로미노
        visited[i][j] = 1
        arr = [(i, j)]
        dfs(i, j, 1, arr)
        visited[i][j] = 0

print(max_s)
