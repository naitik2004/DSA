# class Solution(object):
#     def areaOfMaxDiagonal(self, dimensions):
#         """
#         :type dimensions: List[List[int]]
#         :rtype: int
#         """
#         if not dimensions:
#             return 0

#         max_diag = -1
#         idx = 0

#         for i in range(len(dimensions)):
#             w, h = dimensions[i]
#             diag = w*w + h*h
#             if diag > max_diag:
#                 max_diag = diag
#                 idx = i

#         return dimensions[idx][0] * dimensions[idx][1]

class Solution:
    def areaOfMaxDiagonal(self, dimensions):
        max_diag2 = 0
        max_area = 0

        for l, b in dimensions:
            diag2 = l*l + b*b
            area = l * b
            if diag2 > max_diag2:
                max_diag2 = diag2
                max_area = area
            elif diag2 == max_diag2:
                max_area = max(max_area, area)

        return max_area
