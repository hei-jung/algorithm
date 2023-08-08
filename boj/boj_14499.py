n, m, x, y, k = map(int, input().split())  # 지도 크기 n*m / 주사위 초기 좌표 x,y / 명령 개수 k

grid = []  # 지도
for _ in range(n):
    grid.append(list(map(int, input().split())))

moves = list(map(int, input().split()))  # 이동 명령

dice = [0] * 6  # 주사위 윗면: dice[0] / 주사위 바닥면: dice[5]


# 주사위 굴리기
def roll(di):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if di == 1:  # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif di == 2:  # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif di == 3:  # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    elif di == 4:  # 남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


directions = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]  # 동: 1 / 서: 2 / 북: 3 / 남: 4

for move in moves:
    dx, dy = directions[move]  # 지도에서 이동
    # 주사위는 지도의 바깥으로 이동시킬 수 없다. => 명령 무시
    if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= m:
        continue
    x, y = x + dx, y + dy
    roll(move)  # 주사위 굴리기
    if grid[x][y] == 0:
        grid[x][y] = dice[5]
    else:
        dice[5] = grid[x][y]
        grid[x][y] = 0
    print(dice[0])
