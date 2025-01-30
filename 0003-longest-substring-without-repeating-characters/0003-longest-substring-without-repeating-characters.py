class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0 
        longest = 0
        sett = set()
        n = len(s)

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            sett.add(s[r])
            longest = max(longest, r - l + 1)
        return longest




        # appears = []
        # temp = []
        # count = 0
        # for i in range(len(s)):
        #     if s[i] not in temp:
        #         temp.append(s[i])
        #         count += 1
        #     elif s[i] in temp:
        #         appears.append(count)
                
        #         count = 0
        #         count += 1
        #         del temp[:]
        #         temp.append(s[i])


        # return(max(appears))