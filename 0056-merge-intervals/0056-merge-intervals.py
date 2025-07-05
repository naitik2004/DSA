class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        i = 0
        n = len(intervals)
        while i < n:
            start, end = intervals[i]
            while i + 1 < n and intervals[i+1][0] <= end:
                i += 1
                end  = max(end, intervals[i][1])
            res.append([start,end])
            i += 1

        return res
            
