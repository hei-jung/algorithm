def tornado(r, c):  # 토네이도 구현
    global ans
    sand = a[r][c]
    for dr, dc, rate in direction[d]:
        nr, nc = r + dr, c + dc
        if rate != 0:
            t = int(sand * rate)
        else:  # α (나머지)
            t = a[r][c]
        if 0 <= nr < n and 0 <= nc < n:  # 격자 안에서 이동한 모래
            a[nr][nc] += t  # 모래 이동
        else:  # 격자의 밖으로 나간 모래
            ans += t
        a[r][c] -= t
    return r, c


n = int(input())  # 격자 크기
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

# y 기준 방향과 비율
left = [
    (-1, 1, 0.01), (1, 1, 0.01), (-1, 0, 0.07), (1, 0, 0.07),
    (-2, 0, 0.02), (2, 0, 0.02), (-1, -1, 0.1), (1, -1, 0.1),
    (0, -2, 0.05), (0, -1, 0)
]
down = [(-b, a, rate) for a, b, rate in left]
right = [(a, -b, rate) for a, b, rate in left]
up = [(b, a, rate) for a, b, rate in left]
direction = {0: left, 1: down, 2: right, 3: up}

# y 위치
y = [[0, -1], [1, 0], [0, 1], [-1, 0]]

ans = 0  # 격자 밖으로 이동한 모래의 양
d = 0  # 첫 방향
s = int(n / 2)  # 시작점: 격자의 가운데 칸.
xr, xc = s, s
time = 0
for i in range(2 * n - 1):
    d = i % 4
    if d == 0 or d == 2:
        time += 1
    for _ in range(time):
        yr = xr + y[d][0]
        yc = xc + y[d][1]
        xr, xc = tornado(yr, yc)
print(ans)
