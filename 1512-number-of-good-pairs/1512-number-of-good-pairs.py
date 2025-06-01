import math
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a = {}
        for num in nums:
            if num in a:
                a[num] += 1
            else:
                a[num] = 1
                
        lst = list(a.values())

        total = 0
        for i in lst:
            total += math.factorial(i)//(2*(math.factorial(abs(2-i))))
        return(total)
