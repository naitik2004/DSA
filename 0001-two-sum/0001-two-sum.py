# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

#         indexed_nums = []
#         for num,index in enumerate(nums):
#             indexed_nums.append((index,num))
#         indexed_nums.sort()
#         print(indexed_nums)

#         i = 0
#         j = len(nums)-1
#         res = []
#         while i < j:
#             if indexed_nums[i][0] + indexed_nums[j][0] > target:
#                 j -= 1
#             elif indexed_nums[i][0] + indexed_nums[j][0] < target:
#                 i += 1
#             else:
#                 res.append(indexed_nums[i][1])
#                 res.append(indexed_nums[j][1])
#                 break
#         return res


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         l=[]
#         for i in range (len(nums)):
#             for j in range (i+1,len(nums)):
#                 if nums[i]+nums[j]==target:
#                     l.append(i)
#                     l.append(j)
#         return l


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found