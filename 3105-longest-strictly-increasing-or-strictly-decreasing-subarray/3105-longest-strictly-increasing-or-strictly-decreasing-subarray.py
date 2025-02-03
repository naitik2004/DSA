class Solution(object):  
    def longestMonotonicSubarray(self, nums):  
        incc = 1  
        decc = 1  
        maxx = 1  

        for i in range(len(nums) - 1):  
            if nums[i] < nums[i + 1]:  
                incc += 1  
                decc = 1  
            elif nums[i] > nums[i + 1]:   
                decc += 1  
                incc = 1  
            else:  
                incc = decc = 1  
                
            maxx = max(maxx, decc, incc)  
        
        return maxx