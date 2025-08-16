class Solution(object):
    def maximum69Number (self, num):        
        a = str(num)
        a = a.replace('6','9',1)
        return int(a)

