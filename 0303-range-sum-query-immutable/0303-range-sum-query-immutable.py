class NumArray(object):

    def __init__(self, nums):
        n = len(nums)
        self.prefixSum = [0]*n
        self.prefixSum[0] = nums[0]

        for i in range(1,n):
            self.prefixSum[i] = self.prefixSum[i-1] + nums[i]       

    def sumRange(self, left, right):
        if left == 0:
            ans = self.prefixSum[right]
        else:
            ans = self.prefixSum[right] - self.prefixSum[left-1]
        return ans