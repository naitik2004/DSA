class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indexed_nums = []
        for num,index in enumerate(nums):
            indexed_nums.append((index,num))
        indexed_nums.sort()
        print(indexed_nums)

        i = 0
        j = len(nums)-1
        res = []
        while i < j:
            if indexed_nums[i][0] + indexed_nums[j][0] > target:
                j -= 1
            elif indexed_nums[i][0] + indexed_nums[j][0] < target:
                i += 1
            else:
                res.append(indexed_nums[i][1])
                res.append(indexed_nums[j][1])
                break
        return res


# class Solution(object):
#     def twoSum(self, nums, target):

#         indexed_nums = []
#         for num,index in enumerate(nums):
#             indexed_nums.append((index,num))
#         indexed_nums.sort()
#         print(indexed_nums)

#         a = []
#         left = 0
#         right = len(nums)-1
#         while left < right:
#             curr_sum = indexed_nums[left][0] + indexed_nums[right][0]
#             if curr_sum > target:
#                 right -= 1
#             elif curr_sum < target:
#                 left += 1
#             else:
#                 a.append(indexed_nums[left][1])
#                 a.append(indexed_nums[right][1])

#                 break
#         return(a)
    
