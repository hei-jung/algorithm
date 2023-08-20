n, l = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

cnt = 0


# 행마다 확인하는 함수
def ramp_row(i):
    global cnt
    ramp = [0] * n
    for j in range(n - 1):
        nj = j + 1  # 다음 계단
        if abs(grid[i][nj] - grid[i][j]) > 1:  # 계단의 높이차가 1을 초과함
            return
        if grid[i][nj] > grid[i][j]:  # 다음 계단이 현재 계단보다 1 높은 경우
            for pj in range(l):  # l개 연속인지
                if j - pj < 0 or ramp[j - pj] == 1:  # 범위 벗어나는지 / 이미 경사로가 있는지
                    return
                if grid[i][j - pj] != grid[i][j]:  # 경사로를 놓은 낮은 칸들의 높이가 서로 다름
                    return
                ramp[j - pj] = 1  # 경사로 설치
        elif grid[i][nj] < grid[i][j]:  # 다음 계단이 현재 계단보다 1 낮은 경우
            for pj in range(1, l + 1):
                if j + pj >= n or ramp[j + pj] == 1:
                    return
                if grid[i][j + pj] != grid[i][j] - 1:
                    return
                ramp[j + pj] = 1
    cnt += 1


# 열마다 확인하는 함수
def ramp_col(j):
    global cnt
    ramp = [0] * n
    for i in range(n - 1):
        ni = i + 1  # 다음 계단
        if abs(grid[ni][j] - grid[i][j]) > 1:  # 계단의 높이차가 1을 초과함
            return
        if grid[ni][j] > grid[i][j]:  # 다음 계단이 현재 계단보다 1 높은 경우
            for pi in range(l):  # l개 연속인지
                if i - pi < 0 or ramp[i - pi] == 1:  # 범위 벗어나는지 / 이미 경사로가 있는지
                    return
                if grid[i - pi][j] != grid[i][j]:  # 경사로를 놓은 낮은 칸들의 높이가 서로 다름
                    return
                ramp[i - pi] = 1  # 경사로 설치
        elif grid[ni][j] < grid[i][j]:  # 다음 계단이 현재 계단보다 1 낮은 경우
            for pi in range(1, l + 1):
                if i + pi >= n or ramp[i + pi] == 1:
                    return
                if grid[i + pi][j] != grid[i][j] - 1:
                    return
                ramp[i + pi] = 1
    cnt += 1


for idx in range(n):
    ramp_row(idx)
    ramp_col(idx)

print(cnt)
