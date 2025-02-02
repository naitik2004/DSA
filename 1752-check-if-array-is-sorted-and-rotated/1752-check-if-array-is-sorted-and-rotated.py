class Solution(object):  
    def check(self, nums):  
        if nums[:] == sorted(nums[:]):
            return True
        else:
            l = 0
            while l < len(nums)-1:
                a  = nums.pop(len(nums)-1)
                nums.insert(0,a)
                l+=1
                if nums[:] == sorted(nums[:]):
                    return True
                    break
            return False