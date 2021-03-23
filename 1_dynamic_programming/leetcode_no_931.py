class Solution(object):
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        if n == 1: return matrix[0][0]

        for i in range(1, n):
            matrix[i][0] += min(matrix[i - 1][0], matrix[i - 1][1])
            matrix[i][n - 1] += min(matrix[i - 1][n - 2], matrix[i - 1][n - 1])
            for j in range(1, n - 1):
                matrix[i][j] += min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i - 1][j + 1])

        return min(matrix[n - 1])
