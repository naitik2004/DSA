class Solution(object):
    def search(self, nums, target):
        a = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                a = i
                break

        def binary_search(l, r):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1


        index = binary_search(0, a-1)
        if index == -1:
            index = binary_search(a, len(nums)-1)

        return (index) 
