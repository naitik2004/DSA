class Solution(object):
    def kthFactor(self, n, k):
        a = []
        for i in range(1,n+1):
            if n % i == 0:
                a.append(i)
        if k <= len(a):
            return (a[k-1])
        else:
            return -1
        