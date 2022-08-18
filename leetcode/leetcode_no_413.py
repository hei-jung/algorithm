class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        if n < 3: return 0

        d = nums[1] - nums[0]
        dp = [0] * n
        ans = 0
        for i in range(2, n):
            if nums[i] - nums[i - 1] == d:
                dp[i] = dp[i - 1] + 1
                ans += dp[i]
            else:
                d = nums[i] - nums[i - 1]
        return ans
