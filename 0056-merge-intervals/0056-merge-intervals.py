class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        intervals.sort()
        res=[intervals[0]]
        for i in range(1,len(intervals)):
            if res[-1][1]>=intervals[i][0] and res[-1][1]<intervals[i][1]:
                res[-1][1]=intervals[i][1]
            elif res[-1][1]<intervals[i][0]:
                res.append(intervals[i])
        return res