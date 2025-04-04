class Solution(object):
    def distinctAverages(self, nums):
        nums.sort()

        l = 0
        r = len(nums)-1
        comman = set()
        while (l < r):
            i = ((nums[l]) + (nums[r])) / 2.0
            comman.add(i)
            l += 1
            r -= 1

        return len(comman)