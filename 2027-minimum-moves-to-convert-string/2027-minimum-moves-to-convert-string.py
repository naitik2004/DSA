class Solution(object):
    def minimumMoves(self, s):
        i = 0
        count = 0
        while i < len(s):
            if s[i] == 'X':
                if 'X' in s[i:i+3]:
                    count += 1
                    i += 3
            else:
                i += 1 
        return(count)