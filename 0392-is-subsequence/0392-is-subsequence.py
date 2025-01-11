class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = []
        b = []
        c = []
        count = 0

        for i in range(len(t)):
            a.append(t[i])

        for j in range(len(s)):
            b.append(s[j])

        for l in range(len(a)):
            if count < len(b) and a[l] == b[count]:
                c.append(a[l])
                count += 1

        return(b == c)  
