class Solution(object):
    def maxSubArray(self, nums):
        maxSub = nums[0]
        curSum = 0
        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSub = max(maxSub, curSum)
        return maxSub

        # a = 0 
        # b = -10000

        # for i in nums:
        #     a = a+i
        #     if a > b:
        #         b = a
        #     if a < 0:
        #         a = 0
        # return b
                