"""
{
	"difficulty": "medium",
	"link": "https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/",
	"category": ["greedy"],
	"tags": [],
	"questions": []
}
"""

"""
ATTENTION!!!
	- `lastEnd = min(lastEnd, point[1])`是非常重要的！！！有可能后面的point的end比前面的point的end小
	- 考虑points为空的情况
"""

class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if points:
            points.sort(key=lambda lst: lst[0])
            # print(points)
            lastEnd = points[0][1]
            count = 0
            for point in points:
                if point[0] <= lastEnd:
                    lastEnd = min(lastEnd, point[1])
                    continue
                count += 1
                lastEnd = point[1]
            count += 1
            return count
        else :
            return 0