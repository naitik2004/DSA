class Solution(object):
    def add_sub(self,nums,ans,result,i):
        if i == len(nums):
            result.append(ans)
            return
        self.add_sub(nums, ans + [nums[i]], result, i+1)
        self.add_sub(nums, ans, result, i+1)

    def subsets(self, nums):
        self.result = []
        self.add_sub(nums, [], self.result, 0)
        return self.result

