class Solution(object):
    def minOperations(self, nums, k):
        count = 0
        total = sum(nums)
        
        while total % k != 0:
            max_num = max(nums)
            nums.remove(max_num)        # remove max
            max_num -= 1                # reduce it by 1
            nums.append(max_num)        # put it back
            total -= 1                  # reflect the decrease in sum
            count += 1
        
        return count
