grid = [[0] * 101 for _ in range(101)]
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

n = int(input())  # 드래곤 커브의 개수
for _ in range(n):
    x, y, d, g = map(int, input().split())
    curve = []  # 이전 세대 방향 정보
    grid[y][x] = 1  # 커브 시작점
    ny = y + dy[d]
    nx = x + dx[d]
    grid[ny][nx] = 1  # 0세대 끝점
    curve.append(d)  # 0세대 방향 정보 저장
    for _ in range(g):  # 1세대 이후
        for i in range(len(curve) - 1, -1, -1):
            di = (curve[i] + 1) % 4
            ny += dy[di]
            nx += dx[di]
            grid[ny][nx] = 1
            curve.append(di)

cnt = 0
for y in range(1, 101):
    for x in range(1, 101):
        if grid[y][x] & grid[y - 1][x] & grid[y][x - 1] & grid[y - 1][x - 1]:
            cnt += 1
print(cnt)
