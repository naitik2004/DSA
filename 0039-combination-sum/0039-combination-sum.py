class Solution(object):
    def comSum(self,candidates,i,combin,ans,target):
        if i == len(candidates) or target < 0:
            return
        
        if (target == 0):
            if tuple(combin) not in self.s:  #we use tuple cuz in set list are not allowed
                ans.append(combin[:])
                self.s.add(tuple(combin))
        
        combin.append(candidates[i])
        self.comSum(candidates,i+1,combin,ans,target - candidates[i])
        self.comSum(candidates,i,combin,ans,target - candidates[i])
        combin.pop()
        self.comSum(candidates,i+1,combin,ans,target)


    def combinationSum(self, candidates, target):
        candidates.sort()
        self.ans = []
        self.combin = []
        self.s = set()
        self.comSum(candidates, 0, self.combin, self.ans, target)
        return self.ans


# class Solution(object):
#     def comSum(self, candidates, i, combin, ans, target):
#         if i == len(candidates) or target < 0:
#             return
        
#         if target == 0:
#             if combin[:] not in ans:  # check if this combination already in ans
#                 ans.append(combin[:])
#             return
        
#         combin.append(candidates[i])
#         self.comSum(candidates, i, combin, ans, target - candidates[i])  # can reuse same candidate
#         combin.pop()
#         self.comSum(candidates, i+1, combin, ans, target)  # move to next candidate

#     def combinationSum(self, candidates, target):
#         candidates.sort()
#         ans = []
#         combin = []
#         self.comSum(candidates, 0, combin, ans, target)
#         return ans
