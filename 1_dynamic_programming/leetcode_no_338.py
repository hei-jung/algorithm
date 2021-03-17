class Solution(object):
    def countBits(self, num):
        dp = [0] * (num + 1)
        offset = 1
        for i in range(1, num + 1):
            if i == offset * 2: offset *= 2
            dp[i] = dp[i - offset] + 1
        return dp
