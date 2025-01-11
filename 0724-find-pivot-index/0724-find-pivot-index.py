class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        preSum = [0]*n
        preSum[0] = nums[0]

        for i in range(1, n):
            preSum[i] = preSum[i-1] + nums[i]
        
        for i in range(n):
            leftSum = preSum[i-1] if i > 0 else 0
            rightSum = sum(nums) - preSum[i]
            if leftSum == rightSum:
                return i
                break
        else:
            return -1
