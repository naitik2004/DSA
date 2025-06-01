class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        a = []
        for num in nums:
            sign = -1 if num < 0 else 1
            n = abs(num)
            reversed_num = 0
            
            while n != 0:
                last_digit = n % 10
                reversed_num = reversed_num * 10 + last_digit
                n //= 10
            
            a.append(sign * reversed_num)
        d = a + nums
        return(len(set(d)))
