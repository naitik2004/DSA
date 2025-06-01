class Solution(object):
    def isHappy(self, n):
        a = [] 
        
        while n != 1 and n not in a:
            a.append(n)
            temp = 0
            while n > 0:
                digit = n % 10
                temp += digit * digit
                n //= 10
            n = temp  
        
        return n == 1