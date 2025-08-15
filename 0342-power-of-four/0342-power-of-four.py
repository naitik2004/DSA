class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 1:
            n,r = divmod(n,4)
            if r != 0:
                return False
        if n == 1:
            return True
        else:
            return False
        