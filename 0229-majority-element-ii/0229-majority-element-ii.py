class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a = {}
        res = []
        n = len(nums)
        rep = n/3
        for i in nums:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        for i,j in enumerate(a):
            if a[j] > rep:
                res.append(j)
        return(res)
