class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        a = list(word1)
        b = list(word2)

        a1 = {}
        for i in a:
            if i in a1:
                a1[i] += 1
            else:
                a1[i] = 1

        b1 = {}
        for i in b:
            if i in b1:
                b1[i] += 1
            else:
                b1[i] = 1

        for ch in set(a1.keys() + b1.keys()):
            count1 = a1[ch] if ch in a1 else 0
            count2 = b1[ch] if ch in b1 else 0
            if abs(count1 - count2) > 3:
                return False
        return True
