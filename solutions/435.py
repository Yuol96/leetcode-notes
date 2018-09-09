"""
{
	"difficulty": "medium",
	"link": "https://leetcode.com/problems/non-overlapping-intervals/description/",
	"category": ["greedy"],
	"tags": [],
	"questions": ["Why it works? How does it guarantee the optimal solution?"]
}
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if intervals:
            intervals.sort(key=lambda interval: interval.end)
            lastInterval = intervals[0]
            count = 0
            for idx in range(1,len(intervals)):
                if intervals[idx].start < lastInterval.end:
                    count += 1
                    continue
                lastInterval = intervals[idx]
            return count
        else :
            return 0
