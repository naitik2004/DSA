class Solution(object):
    def isPerfectSquare(self, num):
        l = 0
        r = num
        while l <= r:
            mid = (l + r) // 2
            sqr = mid * mid
            if sqr == num:
                return True
            elif sqr > num:
                r = mid - 1
            else:
                l = mid + 1
        return False       