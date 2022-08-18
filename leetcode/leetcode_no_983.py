class Solution(object):
    def mincostTickets(self, days, costs):
        n = days[-1]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            if i not in days:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[i - 1] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])

        return dp[n]
