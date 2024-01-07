import sys
from collections import deque
input = sys.stdin.readline

board = deque([list(input()) for _ in range(8)])

# 이동 가능 방향
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, 1, 1, 1, 0, -1, -1, -1]

def bfs(x, y):
    q = deque([(x, y)])
    cnt = 0  # 벽 이동 회수
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()  # 캐릭터 현재 위치
            if board[x][y] == '#':
                continue
            if x == 0 and y == 7:
                return 1
            for i in range(9):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                    continue
                if board[nx][ny] == '#':
                    continue
                q.append((nx, ny))
        # 벽 이동
        board.pop()
        board.appendleft(list('........'))
        cnt += 1
        if cnt == 9:
            return 1
    return 0

print(bfs(7, 0))
