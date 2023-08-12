#  이 숫자판의 임의의 위치에서 시작해서, 인접해 있는 네 방향으로 다섯 번 이동하면서, (=> DFS(cnt+1))
#  각 칸에 적혀있는 숫자를 차례로 붙이면 6자리의 수가 된다.
#  이동을 할 때에는 한 번 거쳤던 칸을 다시 거쳐도 되며 (=> DFS),
#  0으로 시작하는 000123과 같은 수로 만들 수 있다. (=> 문자열로 풀어야지)
# 만들 수 있는 수들의 개수를 출력한다. => set()으로 중복 방지
board = []
for _ in range(5):
    board.append(list(input().split()))

numbers = set()
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우


def dfs(x, y, num, cnt):
    if cnt == 5:
        numbers.add(num)
        return
    for dx, dy in directions:
        if 0 <= x + dx < 5 and 0 <= y + dy < 5:
            dfs(x + dx, y + dy, num + board[x + dx][y + dy], cnt + 1)


for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j], 0)

print(len(numbers))
