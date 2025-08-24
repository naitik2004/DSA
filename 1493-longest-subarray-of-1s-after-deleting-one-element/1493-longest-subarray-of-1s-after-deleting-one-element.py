class Solution(object):
    def longestSubarray(self, nums):
        # n = len(nums)

        # prefix = [n]*0
        # if nums[0] == 1:
        #     prefix[0] == 1
        # for i in range(1,n):
        #     if nums[i] == 1:
        #         prefix[i] = prefix[i] + prefix[i-1]
        #     else:
        #         prefix[i] = 0

        # sufix = [0] * n
        # if nums[n - 1] == 1:
        #     sufix[n - 1] = 1
        # for i in range(n - 2,-1,-1):
        #     if nums[i] == 1:
        #         sufix[i] = sufix[i + 1] + 1
        #     else:
        #         sufix[i] = 0
            
        


        curr = 0
        prev = 0
        ans = 0
        
        for i in nums:
            if i == 1:
                curr += 1
            else:
                ans = max(ans, prev + curr)
                prev = curr
                curr = 0

        ans = max(ans, prev + curr)

        if ans == len(nums):
            ans -= 1
        return(ans)
