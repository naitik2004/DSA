class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a = {}
        used = set()

        for i in range(len(s)):
            if s[i] not in a:
                if t[i] not in used:
                    a[s[i]] = t[i]
                    used.add(t[i])

        res = []
        for i in range(len(s)):
            res.append(a[s[i]])

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



