class Solution(object):
    def applyOperations(self, nums):
        i = 0
        j = 1
        while j < len(nums):  
            if nums[i] != nums[j]:
                i += 1
                j += 1
            else:  
                nums[i] *= 2
                nums[j] = 0  
                i += 1
                j += 1

        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1

        a = [0] * count
        nums = [num for num in nums if num != 0]  
        nums.extend(a)
        return nums
