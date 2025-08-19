class Solution(object):
    def zeroFilledSubarray(self, nums):
        ans = 0
        count = 0 
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
                if i+1 == len(nums) or nums[i+1] != 0:
                    ans += count * (count + 1) // 2
                    count = 0
            else:
                count = 0
        return ans
