class Solution(object):
    def a(self, candidates, idx, ans, arr, target):
        if target == 0:
            ans.append(arr[:])
            return
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                break

            arr.append(candidates[i])
            self.a(candidates, i+1, ans, arr, target-candidates[i])
            arr.pop()

    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        arr = []
        self.a(candidates,0,ans,arr,target)
        return ans