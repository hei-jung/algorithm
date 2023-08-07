n, m = map(int, input().split())  # n: 격자 크기 / m: 이동 횟수
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
# 비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다.
cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

for _ in range(m):
    d, s = map(int, input().split())

    # 모든 구름이 di 방향으로 si칸 이동한다.
    moved_cloud = []
    for x, y in cloud:
        x = (x + dx[d] * s) % n
        y = (y + dy[d] * s) % n
        grid[x][y] += 1  # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
        moved_cloud.append((x, y))

    # 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
    visited = [[0] * n for _ in range(n)]
    for r, c in moved_cloud:
        cnt = 0
        for x, y in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            if 0 <= r + x < n and 0 <= c + y < n and grid[r + x][c + y] > 0:
                cnt += 1
        grid[r][c] += cnt
        visited[r][c] = 1

    # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    ans = 0
    new_cloud = []
    for x in range(n):
        for y in range(n):
            if grid[x][y] >= 2 and visited[x][y] != 1:
                grid[x][y] -= 2
                new_cloud.append((x, y))
            ans += grid[x][y]
    cloud = new_cloud

print(ans)
