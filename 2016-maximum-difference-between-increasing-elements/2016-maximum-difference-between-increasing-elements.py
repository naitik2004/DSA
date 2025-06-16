# class Solution:
#     def maximumDifference(self, nums: List[int]) -> int:
#         macx = -1  
#         i = 0
#         j = 1
        
#         while i < len(nums) - 1:
#             while j < len(nums):
#                 if nums[j] > nums[i]:
#                     macx = max(macx, nums[j] - nums[i])
#                 j += 1
#             i += 1
#             j = i + 1

#         return macx

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0]
        max_diff = -1

        for i in range(1, len(nums)):
            if nums[i] > min_val:
                max_diff = max(max_diff, nums[i] - min_val)
            else:
                min_val = nums[i]

        return max_diff
