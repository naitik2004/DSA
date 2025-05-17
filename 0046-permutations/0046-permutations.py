class Solution(object):
    def permute(self, nums):
        ans  = []
        
        def add(nums,idx,ans):
            if idx == len(nums):
                ans.append(nums[:])
                return
            
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                add(nums, idx+1, ans)
                nums[idx], nums[i] = nums[i], nums[idx]
        add(nums,0,ans)
        return ans