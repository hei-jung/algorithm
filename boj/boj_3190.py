from collections import deque

n = int(input())  # 보드 크기
k = int(input())  # 사과 개수
board = [[0] * n for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1
l = int(input())  # 뱀의 방향 변환 횟수
info = dict()  # 방향 회전 정보
for _ in range(l):
    x, c = input().split()  # 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다
    info[int(x)] = c
directions = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])  # 뱀의 초기 방향: 오른쪽


def turn(d):
    if d == 'L':
        directions.rotate(1)
    elif d == 'D':
        directions.rotate(-1)


t = 0
board[0][0] = 2  # 뱀의 초기 상태
snake = deque([(0, 0)])  # 뱀 좌표
i, j = 0, 1  # 뱀 다음 머리 좌표
while 1:
    t += 1
    if t in info:
        turn(info[t])

    # - 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    snake.append((i, j))

    # - 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
    if i < 0 or i >= n or j < 0 or j >= n or board[i][j] == 2:
        break

    # - 만 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    if board[i][j] == 1:
        board[i][j] = 2

    # - 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
    else:
        board[i][j] = 2
        ti, tj = snake.popleft()
        board[ti][tj] = 0

    di, dj = directions[0]
    i = i + di
    j = j + dj

print(t)
