class Solution(object):
    def nextGreatestLetter(self, letters, target):
        left = 0
        right = len(letters)-1
        temp = 0

        while left <= right:
            mid = (left+right)//2

            if letters[mid] > target:
                temp = mid
                right = mid-1
            else:
                left = mid + 1
        return letters[temp]
        
        return letters[temp] 
