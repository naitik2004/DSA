class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        result = 0
        n = len(arr)
        for i in range(n):
            end = i+1
            start = n-i
            total = start * end
            odd = (total+1)//2
            result += odd * arr[i]
        return result