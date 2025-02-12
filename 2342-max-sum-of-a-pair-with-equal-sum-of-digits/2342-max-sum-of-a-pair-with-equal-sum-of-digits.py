class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_groups = {}
        
        for num in nums:

            digit_sum = 0
            temp = num
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
            

            if digit_sum not in digit_sum_groups:
                digit_sum_groups[digit_sum] = (num, 0)  
            else:
                first, second = digit_sum_groups[digit_sum]
                
                if num > first:

                    digit_sum_groups[digit_sum] = (num, first)
                elif num > second:

                    digit_sum_groups[digit_sum] = (first, num)
        

        max_pair_sum = -1
        for first, second in digit_sum_groups.values():
            if second > 0:  
                max_pair_sum = max(max_pair_sum, first + second)
        
        return max_pair_sum