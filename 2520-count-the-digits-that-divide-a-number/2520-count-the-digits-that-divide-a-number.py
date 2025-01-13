class Solution(object):
    def countDigits(self, num):
        count = 0
        a = str(num)
        b = []
        for i in range(len(a)):
            b.append(int(a[i]))

        for i in range(len(b)):
            if num % b[i] == 0:
                count += 1
        return(count)
