class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        # ones = []
        # count = 0
        # for i in range(len(nums)):
        #     if nums[i] == 1:
        #         count += 1
        #     if nums[i] == 0:
        #         ones.append(count)
        #         count = 0
        #     ones.append(count)
        # return max(ones)

        curr = 0
        maxx = 0
        for i in nums:
            if i == 1:
                curr += 1
            else:
                maxx = max(curr, maxx)
                curr = 0
        return max(maxx, curr)





        # currentCount = 0
        # maxCount = 0
        # for num in nums:
        #     if num == 1:
        #         currentCount += 1
        #     else:
        #         maxCount = max(maxCount, currentCount)
        #         currentCount = 0
        # return max(maxCount, currentCount)