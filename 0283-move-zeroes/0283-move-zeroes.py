class Solution(object):
    def moveZeroes(self, nums):
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1

        a = [0]*count
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 0:
                nums.remove(0)

        return nums.extend(a)
