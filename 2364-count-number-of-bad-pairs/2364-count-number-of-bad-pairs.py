class Solution(object):
    def countBadPairs(self, nums):
        n = len(nums)
        freq = {}
        g_pairs = 0
        for i in range(n):
            key = nums[i] - i
            if key in freq:
                g_pairs += freq[key]
            if key in freq:
                freq[key] += 1
            else:
                freq[key] = 1
        b_pirs = n * (n - 1) // 2 - g_pairs
        return(b_pirs)