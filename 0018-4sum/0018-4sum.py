class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        for a in range(len(nums)):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for k in range(a+1, len(nums)):
                if k > a+1 and nums[k] == nums[k-1]:
                    continue

                i = k+1
                j = len(nums)-1

                while i < j:
                    if nums[a] + nums[k] + nums[i] + nums[j] < target:
                        i += 1
                    elif nums[a] + nums[k] + nums[i] + nums[j] > target:
                        j -= 1
                    else:
                        res.append([nums[a], nums[k], nums[i], nums[j]])
                        i += 1
                        j -= 1
                        while i < j and nums[i] == nums[i-1]:
                            i +=1
                        while i < j and nums[j] == nums[j+1]:
                            j -= 1
        return res

            

