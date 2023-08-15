r, c, t = map(int, input().split())
a = []
for _ in range(r):
    # 공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양이다. -1은 2번 위아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있다.
    a.append(list(map(int, input().split())))
for i in range(2, r):
    if a[i][0] == -1:  # 공기청정기는 항상 1번 열에 설치되어 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있다.
        r_up = i
        break
r_down = r_up + 1

directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 반시계 방향


# 1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
def diffusion():
    global a
    diffusion_a = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            # 확산될 미세먼지가 있는 경우
            if a[x][y] > 0:
                pm = int(a[x][y] / 5)  # 확산되는 양은 Ar,c/5이고 소수점은 버린다.
                cnt = 0
                for dx, dy in directions:  # (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
                    nx = x + dx
                    ny = y + dy
                    # 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
                    if nx < 0 or nx >= r or ny < 0 or ny >= c or a[nx][ny] == -1:
                        continue
                    diffusion_a[nx][ny] += pm
                    cnt += 1
                diffusion_a[x][y] += a[x][y] - pm * cnt  # (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.
    a = diffusion_a


# 2. 공기청정기가 작동한다.
def air_clean():
    # 위쪽 공기청정기
    for x in range(r_up - 1, 0, -1):
        a[x][0] = a[x - 1][0]
    for y in range(c - 1):
        a[0][y] = a[0][y + 1]
    for x in range(r_up):
        a[x][c - 1] = a[x + 1][c - 1]
    for y in range(c - 1, 0, -1):
        a[r_up][y] = a[r_up][y - 1]
    a[r_up][0] = -1
    # 아래쪽 공기청정기
    for x in range(r_down + 1, r - 1):
        a[x][0] = a[x + 1][0]
    for y in range(c - 1):
        a[r - 1][y] = a[r - 1][y + 1]
    for x in range(r - 1, r_down, -1):
        a[x][c - 1] = a[x - 1][c - 1]
    for y in range(c - 1, 0, -1):
        a[r_down][y] = a[r_down][y - 1]
    a[r_down][0] = -1


def calculate():
    cnt = 2
    for x in range(r):
        for y in range(c):
            cnt += a[x][y]
    return cnt


for _ in range(t):
    diffusion()
    air_clean()

ans = calculate()
print(ans)
