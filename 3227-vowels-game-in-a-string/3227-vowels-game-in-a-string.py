class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = "AEIOUaeiou"
        count_vowel = 0
        for i in s:
            if i in a:
                count_vowel += 1
        if count_vowel >= 1:
            return True
        else:
            return False
