from collections import deque

# 인접한 칸
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 파이어스톰
# 1. 단계 L 결정: 격자를 2^L * 2^L 크기 부분 격자로 나누고
#   - L을 1부터 Q까지 시전한다는 의미(?)
#   - 부분 격자 시계 방향 90도 회전
def rotate(level):  # l 크기만큼 격자 나눠서 회전
    rotated_graph = [[0] * n for _ in range(n)]
    # 격자 나누기
    for r in range(0, n, level):
        for c in range(0, n, level):
            # 부분 격자 회전
            for i in range(level):
                for j in range(level):
                    rotated_graph[r + i][c + j] = graph[r + level - j - 1][c + i]
    return rotated_graph


# 2. {얼음 있는 칸 3개 이상과 인접해있지 않은 칸 = 얼음 있는 칸 3개 미만과 인접}: 얼음 양 -1
def count_ice(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and tmp[nx][ny] > 0:
            cnt += 1
    if cnt < 3:
        return max(0, tmp[x][y] - 1)
    else:
        return tmp[x][y]


# 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수 구하기
def bfs(x, y):
    s = 0  # 얼음의 합
    cnt = 0  # 칸의 개수
    visited[x][y] = True
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        s += graph[x][y]
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue
            if graph[nx][ny] == 0:
                continue
            visited[nx][ny] = True
            q.append((nx, ny))
    return s, cnt


if __name__ == '__main__':
    # 입력
    N, Q = map(int, input().split())
    n = 2 ** N
    graph = [list(map(int, input().split())) for _ in range(n)]
    L = list(map(int, input().split()))

    # 실행
    for idx in range(Q):
        tmp = rotate(2 ** L[idx])  # 부분 격자 회전
        for r in range(n):
            for c in range(n):
                graph[r][c] = count_ice(r, c)

    sum_ice = 0  # 남아있는 얼음의 합
    max_size = 0  # 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
    visited = [[False] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if graph[r][c] != 0 and not visited[r][c]:
                ice, size = bfs(r, c)
                sum_ice += ice
                if max_size < size:
                    max_size = size

    # 출력
    print(sum_ice)  # 남아있는 얼음 A[r][c]의 합
    print(max_size)  # 가장 큰 덩어리가 차지하는 칸의 개수 (없으면 0)
