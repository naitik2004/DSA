class Solution:
    def nextPermutation(self, nums: List[int]) -> None: 
        i  = len(nums)-2
        while nums[i] >= nums[i+1] and i >=0:
            i -= 1
            
        if i >= 0:
            j = len(nums)-1
            while nums[j] <= nums[i]:
                j -= 1
            nums[j], nums[i] = nums[i], nums[j]

        nums[i+1:] = sorted(nums[i+1:])
        return(nums)


                
