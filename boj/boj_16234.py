from collections import deque

n, l, r = map(int, input().split())  # n: 땅 크기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우


def bfs(x, y):
    q = deque([(x, y)])
    union = []  # 연합 좌표 리스트
    union_cnt = 0  # 연합 크기
    population = 0  # 인구 수
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if l <= abs(graph[x][y] - graph[nx][ny]) <= r and visited[nx][ny] != 1:
                visited[nx][ny] = 1  # 방문 표시
                q.append((nx, ny))  # 다음 번지 지정
                union.append((nx, ny))  # 연합 좌표 저장
                union_cnt += 1
                population += graph[nx][ny]
    if union_cnt > 0:
        new_population = int(population / union_cnt)
        for x, y in union:
            graph[x][y] = new_population
    return union_cnt


day = 0
while 1:
    total_cnt = 0  # 연합을 이루고 있는 총 칸의 개수
    visited = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if visited[x][y] != 1:
                cnt = bfs(x, y)
                total_cnt += cnt
    if total_cnt == 0:  # 연합이 하나도 없으면 종료
        break
    day += 1

print(day)
