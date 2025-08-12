class Solution(object):
    def searchRange(self, nums, target):
        a = -1
        b = -1
        for i in range(len(nums)):
            if nums[i] == target:
                a = i
                break
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == target:
                b = i
                break
        return ([a,b])