class Solution(object):
    def maxAscendingSum(self, nums):
        smax = 0
        maxx = nums[0]
        l = 1
        while(l < len(nums)):
            if nums[l-1] < nums[l]:
                maxx += nums[l]
                l += 1
            elif nums[l-1] > nums[l]:
                smax = maxx
                maxx = 0
                maxx += nums[l]
                l += 1
            smax = max(smax, maxx)
        return smax




        # for i in range(1,len(nums)):
        #     if nums[i-1] < nums[i]:
        #         maxx += nums[i]
        #     else:
        #         smax = max(smax,maxx)
        #         maxx = 0
        # return smax
