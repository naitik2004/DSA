class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        if n%2 == 0:
            return True
        else:
            return False