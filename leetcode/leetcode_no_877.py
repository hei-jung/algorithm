class Solution(object):
    def stoneGame(self, piles):
        l = len(piles)
        if l == 2:
            return True

        dp = [[None for i in range(l)] for j in range(l)]
        parity = 0

        def ans(i, j):

            if dp[i][j] is not None:
                return dp[i][j]
            if i == j:
                return 0
            if i > j:
                return 0

            parity = (j - i + 1) % 2
            if parity == 0:
                dp[i][j] = max(piles[i] + ans(i + 1, j), piles[j] + ans(i, j - 1))
            else:
                dp[i][j] = max(-piles[i] + ans(i + 1, j), -piles[j] + ans(i, j - 1))
            return dp[i][j]

        return ans(0, l - 1) > 0
