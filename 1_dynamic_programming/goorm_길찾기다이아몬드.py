n = int(input())
arr = []
for _ in range(2 * n - 1):
    arr.append(list(map(int, input().split())))

for i in range(1, 2 * n - 1):
    if i < n:
        arr[i][0] += arr[i - 1][0]
        for j in range(1, len(arr[i]) - 1):
            arr[i][j] += max(arr[i - 1][j - 1], arr[i - 1][j])
        arr[i][i] += arr[i - 1][i - 1]
    else:
        for j in range(len(arr[i])):
            arr[i][j] += max(arr[i - 1][j], arr[i - 1][j + 1])

print(arr[-1][-1])
