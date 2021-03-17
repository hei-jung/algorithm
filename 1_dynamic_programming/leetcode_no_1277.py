class Solution(object):
    def countSquares(self, matrix):
        m, n = len(matrix), len(matrix[0])
        dp = [0]*n
        left_top = 0
        cnt = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    top = 0 if i == 0 else dp[j]
                    left = 0 if j == 0 else dp[j-1]
                    dp[j] = 1 + min(min(top, left), left_top)
                    cnt += dp[j]
                    left_top = 0 if j == n-1 else top
                else:
                    dp[j] = 0

        return cnt
