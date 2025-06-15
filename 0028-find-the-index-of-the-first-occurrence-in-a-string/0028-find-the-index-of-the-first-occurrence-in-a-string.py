class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        i = 0
        j, k = 0, 0
        found = False

        while k < len(haystack) and i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    found = True
                    return(k)
                    break
            else:
                k += 1
                i = k
                j = 0

        if not found:
            return(-1)