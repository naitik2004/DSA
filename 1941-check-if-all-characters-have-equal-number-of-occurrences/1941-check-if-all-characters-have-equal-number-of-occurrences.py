class Solution(object):
    def areOccurrencesEqual(self, s):
        a = {}
        for i in s:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1

        val = set(list(a.values()))
        return len(val) == 1


                