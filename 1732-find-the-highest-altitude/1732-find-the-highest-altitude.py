class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a = len(gain)
        altitudes = [0]*(a+1)
        altitudes[0] = gain[0]
        for i in range(1,a):
            altitudes[i] = altitudes[i-1] + gain[i]
        return (max(altitudes))