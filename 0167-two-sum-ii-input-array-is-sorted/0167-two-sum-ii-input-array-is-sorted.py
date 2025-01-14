class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        a = []
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum > target:
                right -= 1
            elif curr_sum < target:
                left += 1
            else:
                a.append(left + 1)
                a.append(right + 1)
                break
        return a