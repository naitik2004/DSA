class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        first_occ = 0
        second_occ = 0
        a = True
        for num in range(len(nums)):
            if nums[num] == target:
                first_occ = num
                a = True
                break
            else:
                a  = False

        if a == True:
            for num in range(len(nums)-1,-1,-1):
                if nums[num] == target:
                    second_occ = num
                    break
            result = [x for x in range(first_occ,second_occ+1)]
            return result
        else:
            return []

