from itertools import combinations

n, m = map(int, input().split())  # n: 도시 크기 / m: 폐업시키지 않을 치킨집 최대 개수
graph = []  # 도시 정보
for _ in range(n):
    graph.append(list(map(int, input().split())))  # 0: 빈 칸 / 1: 집 / 2: 치킨집

house = []  # 집 좌표
chicken = []  # 치킨집 좌표
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

min_dist = 9999  # 도시의 치킨 거리 최솟값

for c in combinations(chicken, m):
    sum_dist = 0  # 모든 집의 치킨 거리의 합
    for h in house:
        dist = 999  # 어떤 집의 치킨 거리
        for i in range(m):
            dist = min(dist, abs(h[0] - c[i][0]) + abs(h[1] - c[i][1]))
        sum_dist += dist
    if min_dist > sum_dist:
        min_dist = sum_dist

print(min_dist)
