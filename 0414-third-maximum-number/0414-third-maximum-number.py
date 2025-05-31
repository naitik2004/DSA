class Solution(object):
    def thirdMax(self, nums):
        a = set(nums)
        if len(a) < 3:
            return max(a)
        else:
            a.remove(max(a))
            a.remove(max(a))
        return max(a)
            