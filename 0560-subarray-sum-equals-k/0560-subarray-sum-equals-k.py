class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        umap = {}
        count = 0
        total = 0
        for i in nums:
            total += i
            if total == k:
                count += 1
            if (total-k) in umap:
                count += umap[total-k]
            
            if total in umap:
                umap[total] += 1
            else:
                umap[total] = 1
        return count