n, m = map(int, input().split())  # 사무실 크기
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))  # 사무실 각 칸 정보

# 방향: 서 => 북 => 동 => 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def get_cctv_dir(cctv_type, d):
    if cctv_type == 1:
        return [(dx[d], dy[d])]
    if cctv_type == 2:
        return [(dx[d], dy[d]), (-dx[d], -dy[d])]
    if cctv_type == 3:
        return [(dx[d], dy[d]), (dx[(d + 1) % 4], dy[(d + 1) % 4])]
    if cctv_type == 4:
        return [(dx[d], dy[d]), (dx[(d + 1) % 4], dy[(d + 1) % 4]), (dx[(d + 2) % 4], dy[(d + 2) % 4])]
    else:
        return [(dx[i], dy[i]) for i in range(4)]


def find_cctv():
    arr = []
    for x in range(n):
        for y in range(m):
            if 1 <= grid[x][y] <= 5:
                arr.append((x, y))
    return arr


cctv = find_cctv()  # 모든 cctv의 위치
n_cctv = len(cctv)  # cctv 개수

min_cnt = 64  # 1 ≤ N, M ≤ 8


# cctv 감시
def watch(i, j, directions):
    for di, dj in directions:
        ni, nj = i, j
        while 1:
            ni += di
            nj += dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                break
            if grid[ni][nj] == 6:
                break
            if grid[ni][nj] != 0:
                continue
            grid[ni][nj] = '#'


# idx번째 cctv 회전
def dfs(idx):
    global min_cnt
    if idx == n_cctv:
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    cnt += 1
        min_cnt = min(min_cnt, cnt)
        return
    x, y = cctv[idx]  # idx번째 cctv 위치
    tmp = []  # grid 복사본
    for d in range(4):  # d가 1 증가할 때마다 90도 방향 회전
        for i in range(n):
            tmp.append([*grid[i]])
        directions = get_cctv_dir(grid[x][y], d)
        watch(x, y, directions)  # (x, y) 위치에 있는 cctv를 directions 방향으로 감시
        dfs(idx + 1)  # 다음 cctv 회전
        for i in range(n):
            grid[i] = [*tmp[i]]  # 원본 복구


dfs(0)
print(min_cnt)
