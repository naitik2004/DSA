class Solution(object):
    def singleNumber(self, nums):
        twice = {}
        for i in nums:
            if i in twice:
                twice[i] += 1
            else:
                twice[i] = 1
        
        for i in twice:
            if twice[i] == 1:
                return i
        