from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)  
        sneaky_numbers = []
        for num, count in counts.items():
            if count == 2:
                sneaky_numbers.append(num)
        return sneaky_numbers