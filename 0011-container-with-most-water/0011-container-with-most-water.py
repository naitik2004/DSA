class Solution(object):
    def maxArea(self, height):
        result = 0
        left, right = 0, len(height) - 1  

        while left < right:

            current_area = min(height[left], height[right]) * (right - left)
            result = max(result, current_area)  
            

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result