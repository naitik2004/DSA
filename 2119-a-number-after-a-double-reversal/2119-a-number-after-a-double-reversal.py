class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s = str(num)
        s = int(s[::-1])
        s = str(s)
        s = int(s[::-1])
        return s == num