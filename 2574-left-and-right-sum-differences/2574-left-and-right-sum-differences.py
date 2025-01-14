class Solution(object):
    def leftRightDifference(self, nums):
        prerSum = [0]*len(nums)

        for i in range(len(nums)-1):
            prerSum[i+1] = prerSum[i] + nums[i]


        suffSum = [0]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            suffSum[i] = suffSum[i+1] + nums[i+1]


        c = [0]*len(nums)
        for i in range(len(nums)):
            c[i] = abs(prerSum[i] - suffSum[i])
        return (c)
