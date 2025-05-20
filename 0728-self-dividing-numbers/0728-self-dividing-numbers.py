class Solution(object):
    def selfDividingNumbers(self, left, right):
        result = []
        for i in range(left, right + 1):
            if self.is_self_dividing(i):
                result.append(i)
        return result

    def is_self_dividing(self, num):
        num_str = str(num)
        for digit in num_str:
            digit = int(digit)
            if digit == 0 or num % digit != 0:
                return False
        return True