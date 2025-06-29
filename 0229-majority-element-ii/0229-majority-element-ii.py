class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]: 
        # Moore's voting algo...
        
        # a = []
        # rep = len(nums)//3
        # test = nums[0]
        # count = 1

        # if len(nums) <= 2:
        #     return nums

        # for i in range(len(nums)):
        #     if count != 0:
        #         if nums[i] == test:
        #             count += 1
        #         else:
        #             count -= 1
        #     elif count > rep:
        #         a.append(nums[i])
        #     else:
        #         test = nums[i]
        #         count = 1
        # return a


            



        a = {}
        res = []
        n = len(nums)
        rep = n/3
        for i in nums:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        for i,j in enumerate(a):
            if a[j] > rep:
                res.append(j)
        return(res)
