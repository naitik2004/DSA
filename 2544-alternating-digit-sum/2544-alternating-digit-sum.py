class Solution(object):
    def alternateDigitSum(self, n):
        total = 0
        z = str(n)
        nums = [i for i in z]
        for i in range(len(nums)):
            if i % 2 == 0:
                total += int(nums[i])
            else:
                total -= int(nums[i])
        return total