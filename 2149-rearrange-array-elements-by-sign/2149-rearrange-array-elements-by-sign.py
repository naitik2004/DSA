class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        nev = []
        for i in nums:
            if i < 0:
                nev.append(i)
            else:
                pos.append(i)
        res = []
        i = 0
        while len(res) != len(nums):
            res.append(pos[i])
            res.append(nev[i])
            i += 1
        return(res)
