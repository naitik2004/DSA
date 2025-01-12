class Solution(object):
    def isFascinating(self, n):
        check = '123456789'
        a = str(n)
        b = str(n*2)
        c = str(n*3)
        total = a+b+c
        if "".join(sorted(total)) == check:
            return True
        else:
            return False

        