n = int(input())  # 수의 개수 (2 ≤ N ≤ 11)
a = list(map(int, input().split()))  # 수열 (1 ≤ Ai ≤ 100)
add, sub, mul, div = map(int, input().split())  # 덧셈, 뺄셈, 곱셈, 나눗셈 개수

res = [-1000000000, 1000000000]  # 연산 결과 최댓값, 최솟값


def dfs(i, tmp):
    global add, sub, mul, div
    if i == n:
        res[0] = max(res[0], tmp)
        res[1] = min(res[1], tmp)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, tmp + a[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, tmp - a[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, tmp * a[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(tmp / a[i]))
            div += 1


dfs(1, a[0])
print(f"{res[0]}\n{res[1]}")
