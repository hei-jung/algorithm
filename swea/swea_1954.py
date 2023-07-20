T = int(input())


def snail(r, c, end):
    # 오른쪽
    if c + 1 < end:
        arr[r][c + 1] = arr[r][c] + 1
        snail(r, c + 1, end)
    # 아래
    elif r + 1 < end:
        arr[r + 1][c] = arr[r][c] + 1
        snail(r + 1, c, end)


def snail_t(r, c, end):
    # 왼쪽
    if c - 1 >= end:
        arr[r][c - 1] = arr[r][c] + 1
        snail_t(r, c - 1, end)
    # 위
    elif r - 1 > end:
        arr[r - 1][c] = arr[r][c] + 1
        snail_t(r - 1, c, end)


for i in range(1, T + 1):
    print(f"#{i}")

    N = int(input())

    arr = [[0] * N for _ in range(N)]
    arr[0][0] = 1

    ans = ""
    k = (N + 1) // 2
    for j in range(N):
        if j < k:
            if 0 < j < N - 1:
                arr[j][j] = arr[j][j - 1] + 1
            snail(j, j, N - j)
            snail_t(N - 1 - j, N - 1 - j, j)
        ans += " ".join(map(str, arr[j]))
        ans += "\n"

    print(ans, end='')
