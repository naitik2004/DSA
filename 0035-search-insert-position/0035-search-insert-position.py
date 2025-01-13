class Solution(object):
    def searchInsert(self, nums, target):
        sm = []
        a = []
        bg = []
        
        for i in range(len(nums)):
            if nums[i] == target:
                return i 
            elif nums[i] < target:
                sm.append(nums[i])
                a.append(i)
            else:
                bg.append(nums[i])
                return i  
        

        return len(nums)



