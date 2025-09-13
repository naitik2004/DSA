class Solution(object):
    def combine(self, n, k):
        nums = []

        for i in range(1,n+1):
            nums.append(i)

        ans = []
        def find(nums,k,idx,curr):
            if len(curr) == k:
                ans.append(curr[:])
                return 

            if idx >= len(nums):
                return 
            
            curr.append(nums[idx])
            find(nums,k,idx+1,curr)
            curr.pop()

            find(nums,k,idx+1,curr)

        find(nums,k,0,[])
        return ans