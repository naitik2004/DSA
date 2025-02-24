import math  

class Solution(object):  
    def minEatingSpeed(self, piles, h):  
        l, r = 1, max(piles)  
        result = r  
        
        while l <= r:  
            mid = (l + r) // 2  
            hours = 0  
             
            hours = sum((pile + mid - 1) // mid for pile in piles)
            
            if hours <= h:  
                result = min(result, mid)  
                r = mid - 1  
            else:  
                l = mid + 1  
                
        return result