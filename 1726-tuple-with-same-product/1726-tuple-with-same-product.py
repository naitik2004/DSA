class Solution(object):
    def tupleSameProduct(self, nums):
        count = 0
        n = len(nums)
        kim = {}
        for i in range(n):
            for j in range(i + 1, n):
                pro = nums[i] * nums[j]
                if pro in kim:
                    kim[pro] += 1
                else:
                    kim[pro] = 1
        for pro in kim:
            sim = kim[pro]
            if sim > 1:
                count += (sim * (sim - 1) // 2) * 8
        return(count)