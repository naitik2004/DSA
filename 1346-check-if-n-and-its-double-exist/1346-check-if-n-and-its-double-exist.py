# class Solution(object):
#     def checkIfExist(self, arr):

#         arr.sort()  
#         for i in range(len(arr)):  
#             left, right = 0, len(arr) - 1  
#             while left <= right:  
#                 mid = (left + right) // 2  
#                 if arr[mid] == 2 * arr[i] and mid != i:  
#                     return True  
#                 elif arr[mid] < 2 * arr[i]:  
#                     left = mid + 1  
#                 else:  
#                     right = mid - 1  
#         return False



class Solution:
    def checkIfExist(self, arr):
        seen = set()
        for num in arr:
            if (2 * num in seen) or (num % 2 == 0 and (num // 2) in seen):
                return True
            seen.add(num)
        return False


