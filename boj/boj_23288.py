from collections import deque

di = 0  # 시계방향: 동 => 남 => 서 => 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dice = [1, 2, 3, 4, 5, 6]


# 점수 계산
def bfs(x, y, b):
    cnt = 0
    visited[x][y] = True
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny]:
                continue
            if MAP[nx][ny] == b:
                visited[nx][ny] = True
                q.append((nx, ny))
        cnt += 1
    return cnt


# 굴리기
def roll():
    global dice
    a, b, c, d, e, f = dice
    if di == 0:  # 동
        dice = [d, b, a, f, e, c]
    elif di == 1:  # 남
        dice = [b, f, c, d, a, e]
    elif di == 2:  # 서
        dice = [c, b, f, a, e, d]
    elif di == 3:  # 북
        dice = [e, a, c, d, f, b]
    return dice[5]


def run(x, y):
    global di
    di = di % 4
    # 1. 이동 방향으로 한 칸 굴러간다
    if x + dx[di] < 0 or x + dx[di] >= N or y + dy[di] < 0 or y + dy[di] >= M:  # 칸 없을 경우
        di = (di + 2) % 4
    x += dx[di]
    y += dy[di]
    a = roll()
    # 2. 도착 칸에 대한 점수 획득
    b = MAP[x][y]
    # 3. 주사위 아랫면에 있는 점수 A와 (x, y)에 있는 점수 B 비교
    if a > b:
        di = (di + 1) % 4
    elif a < b:
        di = (di + 3) % 4
    c = bfs(x, y, b)
    return x, y, b * c


if __name__ == '__main__':
    # 입력
    N, M, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    # 실행
    r, c = 0, 0
    sum_score = 0
    for _ in range(K):
        visited = [[False] * M for _ in range(N)]
        r, c, score = run(r, c)
        sum_score += score

    # 출력
    print(sum_score)
