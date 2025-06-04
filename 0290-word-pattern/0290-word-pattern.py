class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a = s.split()
        
        if len(pattern) != len(a):
            return False
        
        map_s_t = {}
        map_t_s = {}

        for i in range(len(pattern)):
            c1 = pattern[i]
            c2 = a[i]

            if c1 not in map_s_t:
                map_s_t[c1] = c2
            if c2 not in map_t_s:
                map_t_s[c2] = c1

            if map_s_t[c1] != c2 or map_t_s[c2] != c1:
                return False

        return True
