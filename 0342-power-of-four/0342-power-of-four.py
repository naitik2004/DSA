class Solution(object):
    def isPowerOfFour(self, n):
        while n > 1:
            n,r = divmod(n,4)
            if r != 0:
                return False
        if n == 1:
            return True
        return False