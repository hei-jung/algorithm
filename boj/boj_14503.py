n, m = map(int, input().split())  # 방의 크기: n * m
r, c, d = map(int, input().split())  # 처음 위치 (r, c) / 처음 방향 d (0: 북, 1: 동, 2: 남, 3: 서)
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))  # 0: 청소되지 않은 빈칸, 1: 벽

directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]


# 90도 회전
def rotate():
    global d
    if d == 0:
        d = 3
    else:
        d -= 1


cleaned = 0


def dfs(i, j):
    global cleaned
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if graph[i][j] == 0:
        graph[i][j] = -1
        cleaned += 1

    cnt = 0
    for di, dj in directions:
        if 0 <= i + di < n and 0 <= j + dj < m and graph[i + di][j + dj] == 0:
            cnt += 1
            break

    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    if cnt == 0:
        di, dj = directions[d]
        if 0 <= i + di < n and 0 <= j + dj < m and graph[i + di][j + dj] != 1:
            dfs(i + di, j + dj)  # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        else:
            return  # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
    # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    else:
        rotate()  # 반시계 방향으로 90도 회전한다.
        di, dj = directions[d]
        if 0 <= i - di < n and 0 <= j - dj < m and graph[i - di][j - dj] == 0:
            i -= di
            j -= dj  # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        dfs(i, j)  # 1번으로 돌아간다.


dfs(r, c)
print(cleaned)
