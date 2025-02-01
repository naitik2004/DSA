class Solution(object):  
    def isArraySpecial(self, nums):  

        left = 0  
        right = 1   

        while right < len(nums):  

            if nums[left] % 2 == nums[right] % 2:  
                return False  
            
            left += 1  
            right += 1  
 
        return True  
