N, M, K = map(int, input().split())  # N: 격자 크기 / M: 발사한 파이어볼 개수 / K: 이동 명령 횟수

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
grid = [[[] for _ in range(N)] for _ in range(N)]  # 0: 질량(m) / 1: 속력(s) / 2: 방향(d)
fireballs = []

for _ in range(M):
    ri, ci, mi, si, di = map(int, input().split())
    fireballs.append([ri - 1, ci - 1, mi, si, di])

for _ in range(K):
    # 1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
    while fireballs:
        r, c, m, s, d = fireballs.pop()
        r = (r + s * dy[d]) % N
        c = (c + s * dx[d]) % N
        grid[r][c].append([m, s, d])

    for r in range(N):
        for c in range(N):
            cnt = len(grid[r][c])
            # 2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
            if cnt > 1:
                sum_m, sum_s = 0, 0
                d_odd, d_even = 0, 0
                while grid[r][c]:
                    m, s, d = grid[r][c].pop()
                    sum_m += m
                    sum_s += s
                    if d % 2 == 0:
                        d_even += 1
                    else:
                        d_odd += 1
                m = int(sum_m / 5)  # 질량: ⌊(합쳐진 파이어볼 질량의 합)/5⌋
                s = int(sum_s / cnt)  # 속력: ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋
                if cnt == d_odd or cnt == d_even:  # 모두 홀수이거나 모두 짝수
                    directions = [0, 2, 4, 6]
                else:
                    directions = [1, 3, 5, 7]
                if m > 0:  # 질량이 0인 파이어볼은 소멸되어 없어진다.
                    for d in directions:
                        fireballs.append([r, c, m, s, d])
            if cnt == 1:
                m, s, d = grid[r][c].pop()
                fireballs.append([r, c, m, s, d])

# K번 이동 명령 후 남아있는 파이어볼 질량 합
ans = 0
for _, _, m, _, _ in fireballs:
    ans += m
print(ans)
