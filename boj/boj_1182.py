n, s = map(int, input().split())
a = sorted(list(map(int, input().split())))


def dfs(idx, sum):
    global cnt
    if idx >= n:
        return
    sum += a[idx]
    if sum == s:
        cnt += 1
    dfs(idx + 1, sum)  # 현재 원소 선택
    dfs(idx + 1, sum - a[idx])  # 현재 원소 선택x


cnt = 0
dfs(0, 0)
print(cnt)
