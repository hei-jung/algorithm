class Solution(object):
    def countVowelStrings(self, n):
        dp = [1,1,1,1,1]
        for _ in range(n):
            for i in range(1, 5):
                dp[i] += dp[i-1]
        return dp[4]
