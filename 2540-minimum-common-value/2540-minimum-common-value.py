class Solution(object):
    def getCommon(self, nums1, nums2):
        p1 = 0
        p2 = 0
        v = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2] :
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                v = nums1[p1]
                return v
        return -1