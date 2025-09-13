class Solution(object):
    def partition(self, s):
        ans = []
        def find(i, curr):
            if i == len(s):
                ans.append(curr[:])
                return

            for j in range(i, len(s)):
                part = s[i:j+1]
                if part == part[::-1]:
                    curr.append(part)
                    find(j+1,curr)
                    curr.pop()
        find(0,[])
        return ans



# class Solution(object):
#     def isPalidrome(self, part): 
#         s2 = part[::-1]
#         return (part == s2)
                
    
#     def getAllParts(self, s, partitions, ans):
#         if len(s) == 0:
#             ans.append(partitions[:])
#             return

        # for i in range(len(s)):
        #     part = s[:i+1]
        #     if self.isPalidrome(part):
        #         partitions.append(part)
        #         self.getAllParts(s[i+1:], partitions, ans)
        #         partitions.pop()


#     def partition(self, s):
#         self.partitions = []
#         self.ans = []
#         self.getAllParts(s, self.partitions, self.ans)
#         return self.ans