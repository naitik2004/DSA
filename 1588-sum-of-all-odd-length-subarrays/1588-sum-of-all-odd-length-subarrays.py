class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        result = 0
        for length in range(1, len(arr)+1, 2):
            for start in range(len(arr)-length +1):
                result += sum(arr[start:start+length])
        return result