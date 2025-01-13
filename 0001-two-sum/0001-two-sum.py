class Solution(object):
    def twoSum(self, nums, target):

        indexed_nums = []
        for num,index in enumerate(nums):
            indexed_nums.append((index,num))
        indexed_nums.sort()
        print(indexed_nums)

        arr = sorted(nums)

        a = []
        left = 0
        right = len(nums)-1
        while left < right:
            curr_sum = indexed_nums[left][0] + indexed_nums[right][0]
            if curr_sum > target:
                right -= 1
            elif curr_sum < target:
                left += 1
            else:
                a.append(indexed_nums[left][1])
                a.append(indexed_nums[right][1])

                break
        return(a)
    

