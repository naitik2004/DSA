# Approach no.1 

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
#         for i in range(len(queries)):
#             arr = []
#             a = queries[i][0]
#             while a != (queries[i][1])+1:
#                 arr.append(a)
#                 a += 1
#             for k in range(len(arr)):
#                 if nums[arr[k]] > 0:
#                     nums[(arr[k])]  -= 1
#         if sum(nums) == 0:
#             return True
#         else:
#             return False

# Approach no.2                

#         for li, ri in queries:
#             for i in range(li, ri + 1):
#                 if nums[i] > 0:
#                     nums[i] -= 1
#         return all(x == 0 for x in nums)

# Approach no.3

        n = len(nums)
        diff = [0] * (n+1)
        for l,r in queries:
            diff[l] += 1
            if r+1 < n:
                diff[r+1] -= 1

        for i in range(1,n):
            diff[i] = diff[i] + diff[i-1]

        for i in range(n):
            if nums[i] > diff[i]:
                return False

        return True


