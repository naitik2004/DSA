class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if max(nums) >= (sum(nums) - max(nums)):
            return "none"
        else:
            new = set(nums)
            if len(new) == 3:
                return "scalene"
            elif len(new) == 2:
                return "isosceles"
            elif len(new) == 1:
                return "equilateral"