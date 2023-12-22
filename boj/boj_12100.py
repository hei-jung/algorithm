import sys
from copy import deepcopy

input = sys.stdin.readline

N = int(input())  # 보드의 크기
board_init = [list(map(int, input().split())) for _ in range(N)]


# 똑같은 수가 여러 개 있는 경우에는 이동하려고 하는 쪽의 칸이 먼저 합쳐진다
def up(board):
    for c in range(N):
        r = 0
        for i in range(0, N):
            if board[i][c] != 0:
                tmp = board[i][c]
                board[i][c] = 0
                if board[r][c] == 0:
                    board[r][c] = tmp
                elif board[r][c] == tmp:
                    board[r][c] += tmp
                    r += 1
                else:
                    r += 1
                    board[r][c] = tmp
    return board


def down(board):
    for c in range(N):
        r = N - 1
        for i in range(N - 1, -1, -1):
            if board[i][c] != 0:
                tmp = board[i][c]
                board[i][c] = 0
                if board[r][c] == 0:
                    board[r][c] = tmp
                elif board[r][c] == tmp:
                    board[r][c] += tmp
                    r -= 1
                else:
                    r -= 1
                    board[r][c] = tmp
    return board


def left(board):
    for r in range(N):
        c = 0
        for i in range(0, N):
            if board[r][i] != 0:
                tmp = board[r][i]
                board[r][i] = 0
                if board[r][c] == 0:
                    board[r][c] = tmp
                elif board[r][c] == tmp:
                    board[r][c] += tmp
                    c += 1
                else:
                    c += 1
                    board[r][c] = tmp
    return board


def right(board):
    for r in range(N):
        c = N - 1
        for i in range(N - 1, -1, -1):
            if board[r][i] != 0:
                tmp = board[r][i]
                board[r][i] = 0
                if board[r][c] == 0:
                    board[r][c] = tmp
                elif board[r][c] == tmp:
                    board[r][c] += tmp
                    c -= 1
                else:
                    c -= 1
                    board[r][c] = tmp
    return board


directions = {0: up, 1: down, 2: left, 3: right}


def bt(board, depth):
    global ans
    if depth == 5:
        for i in range(N):
            for j in range(N):
                if board[i][j] > ans:
                    ans = board[i][j]
        return
    for d in range(4):
        new_board = deepcopy(board)
        bt(directions[d](new_board), depth + 1)


ans = 0
bt(board_init, 0)
print(ans)
