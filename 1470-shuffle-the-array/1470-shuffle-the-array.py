class Solution(object):
    def shuffle(self, nums, n):
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result


        # a = nums[:n]
        # b = nums[n:]

        # c = []

        # for i in range(n):
        #     c.append(a[i])
        #     c.append(b[i])
        # return(c)
                