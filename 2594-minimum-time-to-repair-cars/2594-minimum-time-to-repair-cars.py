import math  

class Solution(object):
    def repairCars(self, ranks, cars):
        left, right = 1, max(ranks) * cars * cars  
        result = right  
        
        while left <= right:
            mid = (left + right) // 2
            total_cars = 0
            
            for rank in ranks:
                total_cars += math.floor(math.sqrt(mid / rank))
            
            if total_cars >= cars:
                result = min(result, mid)  
                right = mid - 1  
            else:
                left = mid + 1
        
        return result