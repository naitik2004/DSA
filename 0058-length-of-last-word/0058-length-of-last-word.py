class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = list(s.split())
        b = len(a[-1])
        return(b)
        