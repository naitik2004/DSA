class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max_sum = float('-inf')
        # curr_sum = 0
        # for num in nums:
        #     curr_sum = max(num, curr_sum + num)
        #     max_sum = max(curr_sum, max_sum)
        # return max_sum

        cur = 0
        res = nums[0]
        for i in nums:
            cur = max(cur, 0)
            cur += i
            res = max(res, cur)
        return res