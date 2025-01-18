class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = 0  
        n = len(nums)  
        
        for i in range(n):  
            current_diff = abs(nums[i] - nums[(i + 1) % n])  
        
            max_diff = max(max_diff, current_diff)  
        
        return(max_diff)