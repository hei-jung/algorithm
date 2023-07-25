# 선생님은 학생의 순서를 정했고, 각 학생이 좋아하는 학생 4명도 모두 조사했다.
# 이제 다음과 같은 규칙을 이용해 정해진 순서대로 학생의 자리를 정하려고 한다.
# 한 칸에는 학생 한 명의 자리만 있을 수 있고, |r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸이 (r1, c1)과 (r2, c2)를 인접하다고 한다.
# [규칙]
# 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

from collections import deque

n = int(input())
graph = [[0] * n for _ in range(n)]  # 자리
table = dict()  # 조사 표


# 인접한 칸 중에서 좋아하는 학생이 있는 칸 세기
def count_like(x, y, like_list):
    cnt = 0
    if x - 1 >= 0 and graph[x - 1][y] in like_list:
        cnt += 1
    if y - 1 >= 0 and graph[x][y - 1] in like_list:
        cnt += 1
    if y + 1 < n and graph[x][y + 1] in like_list:
        cnt += 1
    if x + 1 < n and graph[x + 1][y] in like_list:
        cnt += 1
    return cnt


# 인접한 칸 중에서 비어있는 칸 세기
def count_space(x, y):
    cnt = 0
    if x - 1 >= 0 and graph[x - 1][y] == 0:
        cnt += 1
    if y - 1 >= 0 and graph[x][y - 1] == 0:
        cnt += 1
    if y + 1 < n and graph[x][y + 1] == 0:
        cnt += 1
    if x + 1 < n and graph[x + 1][y] == 0:
        cnt += 1
    return cnt


# 자리 배치
for _ in range(n ** 2):
    num = list(map(int, input().split()))
    table[num[0]] = num[1:]

    # 1번 규칙
    candidates = [[], [], [], [], []]  # 자리 후보
    for r in range(n):
        for c in range(n):
            # 비어있는 자리가 아닐 경우엔 skip
            if graph[r][c] != 0:
                continue
            candidates[count_like(r, c, table[num[0]])].append((r, c))

    if candidates[4]:
        q = deque(candidates[4])
    elif candidates[3]:
        q = deque(candidates[3])
    elif candidates[2]:
        q = deque(candidates[2])
    elif candidates[1]:
        q = deque(candidates[1])
    else:
        q = deque(candidates[0])

    # 2, 3번 규칙
    candidates = [0] * 5
    while q:
        r, c = q.popleft()
        space = count_space(r, c)
        if candidates[space] == 0:
            candidates[space] = (r, c)

    if candidates[4] != 0:
        r, c = candidates[4]
    elif candidates[3] != 0:
        r, c = candidates[3]
    elif candidates[2] != 0:
        r, c = candidates[2]
    elif candidates[1] != 0:
        r, c = candidates[1]
    else:
        r, c = candidates[0]

    graph[r][c] = num[0]

# print(graph)

# 만족도
score = 0
for r in range(n):
    for c in range(n):
        # 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000
        likes = count_like(r, c, table[graph[r][c]])
        if likes > 0:
            score += 10 ** (likes - 1)

print(score)
