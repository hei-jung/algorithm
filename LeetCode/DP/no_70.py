class Solution(object):
    def climbStairs(self, n):
        a, b = 1, 2
        for i in range(1, n):
            a, b = b, a+b
        return a
