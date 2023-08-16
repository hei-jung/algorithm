from collections import Counter

r, c, k = map(int, input().split())
len_r, len_c = 3, 3
a = []
for _ in range(len_r):
    a.append(list(map(int, input().split())))


def r_op():
    global len_r, len_c
    max_cnt = 0
    tmp = [[0] * 100 for _ in range(100)]
    for i in range(len_r):
        row = []
        for j in range(len(a[i])):
            if a[i][j] != 0:
                row.append(a[i][j])
        # 한 행 또는 열에 있는 수를 정렬하려면, 각각의 수가 몇 번 나왔는지 알아야 한다.
        counter = list(Counter(row).items())
        # 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬
        counter = sorted(counter, key=lambda x: (x[1], x[0]))
        for idx, (num, cnt) in enumerate(counter):
            tmp[i][2 * idx] = num
            tmp[i][2 * idx + 1] = cnt
            max_cnt = max(max_cnt, 2 * (idx + 1))
    len_c = max_cnt
    a.clear()
    for i in range(len_r):
        a.append(tmp[i][:len_c])


def c_op():
    global len_r, len_c
    max_cnt = 0
    tmp = [[0] * 100 for _ in range(100)]
    for j in range(len_c):
        column = []
        for i in range(len_r):
            if a[i][j] != 0:
                column.append(a[i][j])
        # 한 행 또는 열에 있는 수를 정렬하려면, 각각의 수가 몇 번 나왔는지 알아야 한다.
        counter = list(Counter(column).items())
        # 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬
        counter = sorted(counter, key=lambda x: (x[1], x[0]))
        for idx, (num, cnt) in enumerate(counter):
            tmp[2 * idx][j] = num
            tmp[2 * idx + 1][j] = cnt
            max_cnt = max(max_cnt, 2 * (idx + 1))
    len_r = max_cnt
    a.clear()
    for i in range(len_r):
        a.append(tmp[i][:len_c])


for t in range(101):
    if r - 1 < len_r and c - 1 < len_c and a[r - 1][c - 1] == k:
        print(t)
        exit(0)
    if len_r >= len_c:  # R 연산: 배열 A의 모든 행에 대해서 정렬을 수행한다. 행의 개수 ≥ 열의 개수인 경우에 적용된다.
        r_op()
    else:  # C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다. 행의 개수 < 열의 개수인 경우에 적용된다.
        c_op()

print(-1)
