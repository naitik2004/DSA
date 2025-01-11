class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        preSum = [0]*len(nums)
        preSum[0] = nums[0]
        for i in range(1,len(nums)):
            preSum[i] = preSum[i-1] + nums[i]

        for i in range(len(nums)):
            leftSum = preSum[i - 1] if i > 0 else 0
            rightSum = sum(nums) - preSum[i]
            if leftSum == rightSum:
                return(i)
                break
        else:
            return(-1)
