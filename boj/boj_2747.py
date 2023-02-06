n = int(input())

# list 쓰기
dp = [0 for _ in range(n+1)]
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])

# list 없이
first, second = 0, 1
for i in range(n):
    first, second = second, first + second
print(first)