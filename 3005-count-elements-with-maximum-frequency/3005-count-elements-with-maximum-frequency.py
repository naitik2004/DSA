class Solution(object):
    def maxFrequencyElements(self, nums):
        nums.sort()
        a = {}
        b = set(nums)
        for num in nums:
            if num in a:
                a[num] += 1
            else:
                a[num] = 1

        values = sorted(a.values(), reverse=True)

        m = max(values)
        count = 0
        for i in values:
            if i == m:
                count += i
        return(count) 


