class Solution(object):
    def minCost(self, arr, brr, k):  
        n = len(arr)  
        dirCost = 0
        for i in range(n):
            dirCost += abs(arr[i] - brr[i])
        
        if n>1:
            arr.sort()
            brr.sort()

            rearrangedCost = 0
            for i in range(n):
                rearrangedCost += abs(arr[i] - brr[i])

            rearrangedCost += k
            return min(dirCost, rearrangedCost)

        return dirCost