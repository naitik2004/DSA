class Solution(object):
    def findSpecialInteger(self, arr):
        for i in arr:
            if arr.count(i)>(len(arr)//4):
                return i
        
        