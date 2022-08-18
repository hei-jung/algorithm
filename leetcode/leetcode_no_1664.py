class Solution(object):
    def waysToMakeFair(self, nums):
        n = len(nums)
        cnt = 0
        # l[0] <- i 앞 짝수항의 합
        # l[1] <- i 앞 홀수항의 합
        # r[0] <- i 뒤 짝수항의 합
        # r[1] <- i 뒤 홀수항의 합
        l = [0] * 2
        r = [0] * 2

        # i번째 항을 제거하기 전 홀수항 합, 짝수항 합 저장
        for i in range(n):
            r[i % 2] += nums[i]

        for i in range(n):
            r[i % 2] -= nums[i]
            cnt += 1 if l[0] + r[1] == l[1] + r[0] else 0
            l[i % 2] += nums[i]

        return cnt
