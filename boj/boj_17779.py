n = int(input())
a = [[0] * (n + 1)]
for _ in range(n):
    a.append([0] + list(map(int, input().split())))
dist = [[5] * (n + 1) for _ in range(n + 1)]  # 선거구(district)
ans = 1e9


def simulation(x, y, d1, d2):
    global dist, ans
    dist = [[5] * (n + 1) for _ in range(n + 1)]  # 선거구 초기화
    i = 0
    for r in range(1, x + d1):  # 1번 선거구
        if r >= x:
            i += 1
        for c in range(1, y - i + 1):
            dist[r][c] = 1
    i = 0
    for c in range(n, y, -1):  # 2번 선거구
        if c <= y + d2:
            i += 1
        for r in range(1, x + d2 - i + 1):
            dist[r][c] = 2
    i = 0
    for c in range(1, y - d1 + d2):  # 3번 선거구
        if c >= y - d1:
            i += 1
        for r in range(n, x + d1 + i - 1, -1):
            dist[r][c] = 3
    i = 0
    for r in range(n, x + d2, -1):  # 4번 선거구
        if r <= x + d1 + d2:
            i += 1
        for c in range(n, y - d1 + d2 + i - 1, -1):
            dist[r][c] = 4
    # 인구 차이 계산
    population = [0] * 5
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            population[dist[i][j] - 1] += a[i][j]
    population.sort()
    diff = abs(population[4] - population[0])
    ans = diff if diff < ans else ans


for x in range(1, n + 1):
    for y in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                if x + d1 + d2 > n:
                    break
                if y - d1 < 1:
                    break
                if y + d2 > n:
                    break
                simulation(x, y, d1, d2)

print(ans)
