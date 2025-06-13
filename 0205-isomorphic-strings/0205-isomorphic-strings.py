class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a = {}
        used = set()

        for i in range(len(s)):
            if s[i] in a:
                if a[s[i]] != t[i]:
                    return False
            else:
                if t[i] in used:
                    return False
                a[s[i]] = t[i]
                used.add(t[i])

        res = []
        for i in s:
            res.append(a[i])
        ans = "".join(res)

        return ans == t




# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         a = {}
#         for i in range(len(s)):
#             if s[i] in a:
#                 continue
#             else:
#                 a[s[i]] = t[i]

#         res = []
#         for i in s:
#             res.append(a[i])
#         ans =  "".join(res)

#         if ans == t:
#             return True
#         return False



