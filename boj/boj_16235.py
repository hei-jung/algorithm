### PyPy3로 통과했지만 Python3로는 통과 못함
from collections import deque

n, m, k = map(int, input().split())  # n: 땅 크기, m: 나무 개수, k: 종료 조건
grid = [[5] * n for _ in range(n)]  # 가장 처음에 양분은 모든 칸에 5만큼 들어 있음
a = []  # S2D2 양분
for _ in range(n):
    a.append(list(map(int, input().split())))
trees = [[deque() for _ in range(n)] for _ in range(n)]  # 나무 정보
for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for _ in range(k):
    for r in range(n):
        for c in range(n):
            n_tree = len(trees[r][c])
            for i in range(n_tree):  # 나이가 어린 나무부터
                if trees[r][c][i] > grid[r][c]:  # 양분이 부족하면 즉시 죽음
                    for _ in range(i, n_tree):
                        grid[r][c] += int(trees[r][c].pop() / 2)  # 죽은 나무마다 나이를 2로 나눈 값이 양분으로 추가됨(소수점 버림)
                        m -= 1
                    break
                grid[r][c] -= trees[r][c][i]  # 나무 나이만큼 양분 먹음
                trees[r][c][i] += 1  # 나이 1 증가
    for r in range(n):
        for c in range(n):
            for age in trees[r][c]:  # 나무 번식
                if age % 5 == 0:
                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            trees[nr][nc].appendleft(1)
                            m += 1
            grid[r][c] += a[r][c]  # 양분 추가

print(m)
