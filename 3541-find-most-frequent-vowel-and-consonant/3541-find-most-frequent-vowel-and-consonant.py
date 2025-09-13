class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """

        vowel = "aeiou"

        vowel_dict = {}
        cons_dict = {}

        for vo in s:
            if vo in vowel:
                if vo in vowel_dict:
                    vowel_dict[vo] += 1
                else:
                    vowel_dict[vo] = 1
            else:
                if vo in cons_dict:
                    cons_dict[vo] += 1
                else:
                    cons_dict[vo] = 1

        max_vowel = max(vowel_dict.values()) if vowel_dict else 0 
        max_cons = max(cons_dict.values()) if cons_dict else 0

        return max_vowel + max_cons






        