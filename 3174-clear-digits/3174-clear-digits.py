class Solution(object):
    def clearDigits(self, s):
        n = len(s)
        new_s = list(s)
        i = 0
        while i < len(new_s):
            if new_s[i].isdigit():
                if i > 0:
                    new_s.pop(i)
                    new_s.pop(i - 1)
                    i -= 1
                else:
                    new_s.pop(i)
            else:
                i += 1
        s = "".join(new_s)
        return(s)