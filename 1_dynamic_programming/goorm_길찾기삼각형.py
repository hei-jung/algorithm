n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n):
    arr[i][0] += arr[i - 1][0]
    for j in range(1, i):
        arr[i][j] += max(arr[i - 1][j - 1], arr[i - 1][j])
    arr[i][i] += arr[i - 1][i - 1]

print(max(arr[-1]))
