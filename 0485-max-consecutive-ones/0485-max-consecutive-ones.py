class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        ones = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            if nums[i] == 0:
                ones.append(count)
                count = 0
            ones.append(count)
        return max(ones)

