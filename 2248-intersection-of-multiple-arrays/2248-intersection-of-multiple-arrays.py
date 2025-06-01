class Solution(object):
    def intersection(self, nums):
        a = {}
        for sublist in nums:
            for num in sublist:
                if num in a:
                    a[num] += 1
                else:
                    a[num] = 1
        b = []
        for i in a:
            if a[i] == len(nums):
                b.append(i)
        return sorted(b)
