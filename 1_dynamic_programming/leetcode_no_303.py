class NumArray(object):

    def __init__(self, nums):
        # ﻿NumArray initializes the object with the integer array nums.﻿
        # 멤버 변수 nums를 만들고, 입력 받은 nums 배열로 초기화 해준다.
        self.nums = nums

    def sumRange(self, i, j):
        # ﻿Return the sum of the elements of the nums array in ﻿the range [i, j] inclusive
        # i에서 j까지의 합을 return한다.
        return sum(self.nums[i:j + 1])