from collections import deque

n = int(input())  # 공간의 크기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 아기 상어 처음 크기: 2
baby_shark = 2
# 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.
directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def initial_pos():
    for x in range(n):
        for y in range(n):
            if graph[x][y] == 9:
                graph[x][y] = 0
                return x, y


def bfs(x, y):
    global time, baby_shark, eat_cnt
    q = deque([(x, y)])
    fish_arr = []
    dist = 0
    while q:
        dist += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if graph[nx][ny] > baby_shark or visited[nx][ny] == 1:
                    continue
                if 0 < graph[nx][ny] < baby_shark:  # 먹을 수 있는 물고기
                    fish_arr.append((nx, ny, dist))
                q.append((nx, ny))
                visited[nx][ny] = 1
    return sorted(fish_arr, key=lambda k: (k[2], k[0], k[1]))


i, j = initial_pos()
time = 0
eat_cnt = 0
while 1:
    visited = [[0] * n for _ in range(n)]
    visited[i][j] = 1
    fish = bfs(i, j)
    if not fish:
        break
    i, j, d = fish[0]
    eat_cnt += 1  # 냠냠
    graph[i][j] = 0  # 물고기를 먹으면 그 칸은 빈칸이 된다.
    time += d
    if eat_cnt == baby_shark:  # 자신의 크기와 같은 수의 물고기를 먹을 때마다,
        baby_shark += 1  # 크기가 1 증가
        eat_cnt = 0

print(time)
