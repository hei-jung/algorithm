from collections import deque

# 입력 값 받기
n, m = map(int, input().split())  # n: 격자 한 변의 크기 / m: 색상의 개수
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))


# 블록 그룹 크기 계산
def bfs(x, y):
    group_visited = []  # 그룹 내 블록 좌표 저장
    q = deque()
    q.append((x, y))
    cnt = 0  # 블록 그룹 크기
    rainbow_cnt = 0  # 무지개 블록 개수
    while q:
        i, j = q.popleft()
        if (i, j) not in group_visited:
            group_visited.append((i, j))
        cnt += 1
        if grid[i][j] == 0:
            rainbow_cnt += 1
        if i - 1 >= 0 and (i - 1, j) not in group_visited:
            if grid[i - 1][j] == grid[x][y] or grid[i - 1][j] == 0:
                group_visited.append((i - 1, j))
                q.append((i - 1, j))
        if i + 1 < n and (i + 1, j) not in group_visited:
            if grid[i + 1][j] == grid[x][y] or grid[i + 1][j] == 0:
                group_visited.append((i + 1, j))
                q.append((i + 1, j))
        if j - 1 >= 0 and (i, j - 1) not in group_visited:
            if grid[i][j - 1] == grid[x][y] or grid[i][j - 1] == 0:
                group_visited.append((i, j - 1))
                q.append((i, j - 1))
        if j + 1 < n and (i, j + 1) not in group_visited:
            if grid[i][j + 1] == grid[x][y] or grid[i][j + 1] == 0:
                group_visited.append((i, j + 1))
                q.append((i, j + 1))
    return sorted(group_visited), cnt, rainbow_cnt


# 제일 큰 블록 그룹 찾기
def find_max_group():
    visited = []  # 모든 방문 좌표 저장
    max_arr = []  # 블록 그룹 좌표 저장
    max_area = 1  # 블록 그룹 최대 크기
    max_rainbow = 0  # 무지개 블록 최대 개수
    for i in range(n):
        for j in range(n):
            # 이미 방문한 블록이면 skip
            if (i, j) in visited:
                continue
            # 빈 칸 / 검은색 블록 / 무지개 블록은 기준 블록으로 쓰지 않음
            if grid[i][j] != "X" and grid[i][j] != -1 and grid[i][j] != 0:
                arr, area, rainbow = bfs(i, j)
                visited += arr  # 방문 좌표 저장
                # 크기가 큰 블록 그룹
                if area > max_area:
                    max_arr = arr
                    max_area = area
                    max_rainbow = rainbow
                # 크기가 큰 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹
                elif area == max_area and rainbow > max_rainbow:
                    max_arr = arr
                    max_rainbow = rainbow
                # 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을, 그것도 여러개이면 열이 가장 큰 것을 찾는다.
                elif area == max_area and rainbow == max_rainbow:
                    max_arr = arr
    return max_arr, max_area


# 중력 작용을 위한 탐색
def dfs(i, j, color):
    # 아랫칸이 빈칸
    if i + 1 < n and grid[i + 1][j] == 'X':
        grid[i][j] = 'X'
        dfs(i + 1, j, color)
    else:
        grid[i][j] = color
        return


# 중력 작용
def gravity():
    for j in range(n):
        for i in range(n):
            # 맨 아래 칸부터
            if grid[n - 1 - i][j] == -1:
                continue
            elif grid[n - 1 - i][j] != 'X':
                dfs(n - 1 - i, j, grid[n - 1 - i][j])


# 90도 반시계 방향으로 회전
def rotate():
    rotated_grid = [[0] * n for _ in range(n)]
    for j in range(n):
        for i in range(n):
            rotated_grid[j][i] = grid[i][n - 1 - j]
    return rotated_grid


score = 0

while 1:
    max_group, b = find_max_group()

    # 블록 그룹이 존재하지 않으면 종료
    if b < 2:
        break

    # 블록 제거
    for (r, c) in max_group:
        grid[r][c] = 'X'
    score += b ** 2

    # 중력 작용
    gravity()

    # 90도 반시계 방향으로 회전
    grid = rotate()

    # 중력 작용
    gravity()

print(score)
