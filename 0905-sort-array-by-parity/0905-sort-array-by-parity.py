class Solution(object):
    def sortArrayByParity(self, nums):
        l = 0  
        r = len(nums) - 1  

        while l < r:  
            while l < r and nums[l] % 2 == 0:  
                l += 1  
            while l < r and nums[r] % 2 == 1:  
                r -= 1  
            if l < r:  
                nums[l], nums[r] = nums[r], nums[l]  

        return(nums)


