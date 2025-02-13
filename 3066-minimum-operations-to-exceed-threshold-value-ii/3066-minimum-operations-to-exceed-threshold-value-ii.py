class Solution:
    import heapq  
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)  
        operations = 0  

        while len(nums) > 1 and nums[0] < k:  
            smallest = heapq.heappop(nums)  
            second_smallest = heapq.heappop(nums)  
            
            new_number = min(smallest, second_smallest) * 2 + max(smallest, second_smallest)  
            
            heapq.heappush(nums, new_number)  
            
            operations += 1  
        
        while nums and nums[0] < k:  
            smallest = heapq.heappop(nums)  
            if len(nums) > 0:  
                second_smallest = heapq.heappop(nums)  
                new_number = min(smallest, second_smallest) * 2 + max(smallest, second_smallest)  
                heapq.heappush(nums, new_number)  
                operations += 1  
        
        return operations  
