n, m, h = map(int, input().split())  # n: 세로선 개수 / m: 가로선 개수 / h: 세로선마다 가로선을 놓을 수 있는 위치의 개수
grid = [[0] * (h + 1) for _ in range(n + 1)]

for _ in range(m):
    # b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결했다
    a, b = map(int, input().split())  # 가로선 정보 (1 ≤ a ≤ H, 1 ≤ b ≤ N-1)
    grid[b][a] = b + 1
    grid[b + 1][a] = b


# 사다리 게임은 각각의 세로선마다 게임을 진행하고, 세로선의 가장 위에서부터 아래 방향으로 내려가야 한다.
# 이때, 가로선을 만나면 가로선을 이용해 옆 세로선으로 이동한 다음, 이동한 세로선에서 아래 방향으로 이동해야 한다.
def sadari():
    for c in range(1, n + 1):
        idx = c
        for r in range(1, h + 1):
            # 가로선이 있니?
            if grid[idx][r]:
                idx = grid[idx][r]
        if idx != c:
            return False
    return True


ans = 4


def dfs(cnt):
    global ans
    if sadari():
        ans = ans if ans < cnt else cnt
    elif cnt == 3 or ans <= cnt:
        return
    for c in range(1, n):
        flag = False
        for r in range(1, h + 1):
            if flag and grid[c][r] == 0 and grid[c + 1][r] == 0:
                continue
            else:
                flag = False
            if grid[c][r] == 0 and grid[c + 1][r] == 0:
                grid[c][r] = c + 1
                grid[c + 1][r] = c
                dfs(cnt + 1)
                grid[c][r] = 0
                grid[c + 1][r] = 0
                flag = True


dfs(0)
print(ans if ans < 4 else -1)
