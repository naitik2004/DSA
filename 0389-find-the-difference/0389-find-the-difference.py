class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_chars = list(s)
        t_chars = list(t)

        for char in s_chars:
            if char in t_chars:
                t_chars.remove(char)
            
        return t_chars[0]