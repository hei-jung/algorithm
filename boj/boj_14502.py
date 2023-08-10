from collections import deque
from itertools import combinations

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))  # 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

#  안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.
max_safe_zone = 0

space = []
virus = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            space.append((i, j))  # 빈칸 좌표 저장
        elif graph[i][j] == 2:
            virus.append((i, j))  # 바이러스 좌표 저장


def bfs(infected_graph):
    global max_safe_zone
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and infected_graph[nx][ny] == 0:
                q.append((nx, ny))  # 다음 방문 좌표로 지정
                infected_graph[nx][ny] = 2  # 바이러스 퍼짐
    safe_zone = 0
    for x in range(n):
        for y in range(m):
            if infected_graph[x][y] == 0:
                safe_zone += 1
    max_safe_zone = safe_zone if safe_zone > max_safe_zone else max_safe_zone


#  새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
for wall in combinations(space, 3):
    defenced_graph = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if (i, j) in wall:
                defenced_graph[i][j] = 1  # 벽 세우기
            else:
                defenced_graph[i][j] = graph[i][j]
    bfs(defenced_graph)  # 바이러스 전염

print(max_safe_zone)
