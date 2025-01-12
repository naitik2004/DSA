class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0
        for i in stones:
            if i not in jewels:
                count += 1
        a = len(stones) - count
        return(a)
