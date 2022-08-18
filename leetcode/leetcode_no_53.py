class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        dp = [nums[0]]
        for i in range(1, n):
            dp.append(max(nums[i], dp[i-1]+nums[i]))
        return max(dp)