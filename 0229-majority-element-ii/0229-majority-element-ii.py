class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]: 
        # Moore's voting algo...
        if len(nums) < 2:
            return nums

        res = []
        first = nums[0]
        second = None
        fc = 1
        sc = 0
        for i in range(len(nums)):
            if first == nums[i]:
                first = nums[i]
                fc += 1
            elif second == nums[i]:
                second = nums[i]
                sc += 1
            elif fc == 0:
                first = nums[i]
                fc = 1
            elif sc == 0:
                second = nums[i]
                sc = 1
            else:
                fc -= 1
                sc -= 1
        
        fc = 0
        sc = 0
        for i in nums:
            if first == i:
                fc += 1
            if second == i:
                sc += 1
        
        a = len(nums)//3
        if fc > a:
            res.append(first)
        if sc > a:
            res.append(second)
        
        return res


            



        # a = {}
        # res = []
        # n = len(nums)
        # rep = n/3
        # for i in nums:
        #     if i in a:
        #         a[i] += 1
        #     else:
        #         a[i] = 1
        # for i,j in enumerate(a):
        #     if a[j] > rep:
        #         res.append(j)
        # return(res)
