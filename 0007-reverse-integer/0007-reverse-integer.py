class Solution(object):
    def reverse(self, x):
        x = str(x)
        if "-" in x:
            x = x.replace("-", "")
            x = "-" + x[::-1]
            x = int(x)
        else:
            x = "".join(list(x[::-1]))
            x = int(x)
        
        if x < -2**31 or x > 2**31 - 1:
            return 0
        return x









    def reverse(self, x):
        is_negative = x < 0
        x = abs(x)
        
        reversed_x = 0
        while x != 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10
        
        if is_negative:
            reversed_x = -reversed_x
        
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        
        return reversed_x