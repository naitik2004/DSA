class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        a = {}
        for i in arr:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1

        c = []
        for key, value in a.items():
            c.append([key, value])

        b = []
        for i in range(len(c)):
            if c[i][1] == 1:
                b.append(c[i])

        if len(b) < k:
            return("")
        else:
            return(b[k-1][0])

