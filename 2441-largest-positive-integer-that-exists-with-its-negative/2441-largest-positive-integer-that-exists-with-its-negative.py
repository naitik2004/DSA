class Solution(object):
    def findMaxK(self, nums):

        nums.sort()
        l = 0
        r = len(nums)-1

        final = 0

        while l < r:
            if nums[l] + nums[r] == 0:
                return nums[r]
            elif nums[l] + nums[r] < 0 :
                l += 1
            else:
                r -= 1
        return -1