# class Solution:
#     def singleNonDuplicate(self, nums: List[int]) -> int:
#         l = 0
#         r = len(nums) - 1
#         while l <= r:
#             mid = (l + r) // 2
#             if mid > 0 and (mid - l) % 2 == 0 and nums[mid - 1] == nums[mid]:
#                 l = mid + 1
#             elif mid < len(nums) - 1 and (r - mid) % 2 == 0 and nums[mid + 1] == nums[mid]:
#                 r = mid - 1
#             else:
#                 return nums[mid]



class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2

            if mid > 0 and nums[mid] == nums[mid - 1]:
                mid -= 1
                if (mid - l) % 2 == 0:
                    l = mid + 2
                else:
                    r = mid - 1

            elif mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                if (mid - l) % 2 == 0:
                    l = mid + 2
                else:
                    r = mid - 1
                    
            else:
                return nums[mid]
        return nums[l]
