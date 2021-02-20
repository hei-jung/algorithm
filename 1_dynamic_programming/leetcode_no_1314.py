class Solution(object):
    def matrixBlockSum(self, mat, K):
        m, n = len(mat), len(mat[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        answer = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] - dp[i][j] + mat[i][j]

        for i in range(m):
            r_min = max(0, i - K)
            r_max = min(m, i + K + 1)
            for j in range(n):
                c_min = max(0, j - K)
                c_max = min(n, j + K + 1)
                answer[i][j] = dp[r_min][c_min] + dp[r_max][c_max] - dp[r_min][c_max] - dp[r_max][c_min]

        return answer