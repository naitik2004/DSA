from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_map = defaultdict(int)
        sum_map[0] = 1
        
        curr_sum = 0
        count = 0
        for i in nums:
            curr_sum += i 
            if curr_sum - k in sum_map:
                count += sum_map[curr_sum - k]
            sum_map[curr_sum] += 1
        return count