class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        dp = [0] * n
        dp[0] = 1.0
        for i in range(1, n):
            dp[i] = 1.0 / (i + 1) + dp[i - 1] * (i - 1) / (i + 1)
        return dp[-1]
