import sys
input = sys.stdin.readline

m, n = map(int, input().split())

# 오른쪽 => 아래 => 왼쪽 => 위
dx = [0,1,0,-1]
dy = [1,0,-1,0]

a = [[0]*n for _ in range(m)]
a[0][0] = 1
x, y = 0, 0  # 시작점
d = 0  # 방향
visited_cnt = 1  # 방문 좌표 개수

cnt = 0
while 1:
    if visited_cnt == m*n:
        break
    nx = x + dx[d]
    ny = y + dy[d]
    if nx < 0 or nx >= m or ny < 0 or ny >= n or a[nx][ny]:
        cnt += 1
        d = (d+1) % 4
    else:
        a[nx][ny] = 1
        visited_cnt += 1
        x = nx
        y = ny

print(cnt)
