class Solution(object):
    '''실패 - 다시 풀어야 함'''
    def numSubmat(self, mat):
        rows, cols = len(mat), len(mat[0])
        dp = [[0] * cols for _ in range(rows)]
        nums = [0] * cols
        sum = 0

        for i in range(rows):
            for j in range(cols):
                if j == 0:
                    nums[j] = mat[i][j]
                else:
                    if mat[i][j] == 0:
                        nums[j] = 0
                    else:
                        nums[j] = nums[j - 1] + 1
                if i == 0:
                    dp[i][j] = nums[j]
                    sum += dp[i][j]
                else:
                    if nums[j] == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i - 1][j] + nums[j]
                        sum += dp[i][j]
            print(f"{i}th row: {nums}")

        print(dp)

        return sum


# mat = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
mat = [[1, 1, 1, 1, 1, 1]]
ans = Solution.numSubmat(Solution, mat)
print(ans)
