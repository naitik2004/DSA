class Solution(object):
    def searchRange(self, nums, target):
        l = 0
        r = len(nums) - 1
        lst = [-1, -1]

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                a = mid 
                b = mid 

                while a >= 0 and nums[a] == target:
                    a -= 1
                lst[0] = a + 1

                while b < len(nums) and nums[b] == target:
                    b += 1
                lst[1] = b - 1

                return lst

            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return lst
