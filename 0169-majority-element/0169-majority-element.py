class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = 0 
        count = 0
        for i in range(len(nums)):
            if count == 0:
                ans = nums[i]

            if ans == nums[i]:
                count += 1
            else:
                count -= 1
        return ans



        # n = (len(nums)//2)
        # a = {}
        # for i in nums:
        #     if i in a:
        #         a[i] += 1
        #     else:
        #         a[i] = 1

        # for i, v in enumerate(a):
        #     if a[v] > n:
        #         return(v)


