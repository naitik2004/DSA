class Solution(object):
    def searchMatrix(self, matrix, target):
        temp = []
        a = 0
        for i in matrix:
            if i[-1] >= target:
                temp = i
                break
        
        for j in temp:
            if j == target:
                return True

        return False
