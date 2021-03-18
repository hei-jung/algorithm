class Solution(object):
    def mctFromLeafValues(self, arr):
        n = len(arr)
        dp = [[0] * n for _ in range(n)]

        for x in range(1, n):
            for i in range(0, n - x):
                j = i + x
                if x == 1:
                    dp[i][j] = arr[i] * arr[j]
                else:
                    for k in range(i, j):
                        if dp[i][j] == 0:
                            dp[i][j] = dp[i][k] + dp[k + 1][j] + max(arr[i:k + 1]) * max(arr[k + 1:j + 1])
                        else:
                            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + max(arr[i:k + 1]) * max(arr[k + 1:j + 1]))

        return dp[0][n - 1]

