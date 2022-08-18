n = int(input())
arr = list(map(int, input().split()))
dp = [1]

for i in range(1, n):
    if arr[i] > arr[i - 1]:
        dp.append(dp[i - 1] + 1)
    else:
        dp.append(dp[0])

print(max(dp))
