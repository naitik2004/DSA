class Solution(object):
    def sortVowels(self, s):
        vowels = set('AEIOUaeiou')
        freq = {}
        for ch in s:
            if ch in vowels:
                if ch in freq:
                    freq[ch] += 1
                else:
                    freq[ch] = 1
        sorted_vowels = []
        for ch in sorted(freq.keys()):
            for j in range(freq[ch]):
                sorted_vowels.append(ch)
        s = list(s)
        idx = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = sorted_vowels[idx]
                idx += 1
        return ''.join(s)
