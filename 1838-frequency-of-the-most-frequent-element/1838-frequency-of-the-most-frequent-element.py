class Solution(object):
    def maxFrequency(self, nums, k):
        # samples = []
        nums.sort()
        # temp = k
        # i = len(nums) - 2
        # j = len(nums) - 1

        # count = 1
    
        # while i >= 0:
        #     diff = nums[j] - nums[i]
        #     if temp >= diff:
        #         temp -= diff
        #         count += 1
        #         i -= 1
        #     else:
        #         j -= 1
        #         samples.append(count)
        #         count = 1
        #         i = j - 1
        #         temp = k
        
        # samples.append(count) 
        # return (max(samples))

        res, total = 0,0
        l, r = 0,0
        while r < len(nums):
            total += nums[r]
            while nums[r]*(r-l+1) > total + k:
                total -= nums[l]
                l += 1
            res = max(res, r-l+1) 
            r += 1
        return res           