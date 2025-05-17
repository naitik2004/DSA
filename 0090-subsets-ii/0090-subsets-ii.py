class Solution(object):
    def add_sub(self,nums,ans,result,i):
        if i == len(nums):
            result.append(list(ans))
            return
            
        ans.append(nums[i])
        self.add_sub(nums, ans, result, i+1)
        ans.pop()

        idx = i+1
        while idx < len(nums) and nums[idx] == nums[idx -1]:
            idx += 1

        self.add_sub(nums, ans, result, idx)
                

    def subsetsWithDup(self, nums):
        nums.sort()
        result = []
        self.add_sub(nums, [], result, 0)
        return result

