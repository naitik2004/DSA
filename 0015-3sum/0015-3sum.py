class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i = k+1
            j = len(nums)-1
            while i < j:
                if nums[k] + nums[i] + nums[j] < 0:
                    i += 1
                elif nums[k] + nums[i] + nums[j] > 0:
                    j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i-1] == nums[i]:
                        i +=1
                    while i < j and nums[j+1] == nums[j]:
                        j -= 1
        return res

            





        # res = []
        # unique_combos = set(tuple(sorted(c)) for c in combinations(nums, 3))
        # a = list(unique_combos)
        # for i in range(len(a)):
        #     if sum(a[i]) == 0:
        #         res.append(a[i])
        # return res

