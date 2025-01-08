class Solution(object):
    def majorityElement(self, nums):
        avg = len(nums)//2
 
        var = set(nums)
        myList = list(var)


        for i in range(len(myList)):
            final = nums.count(myList[i])
            if final > avg:
                return(myList[i])


        