"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/daily-temperatures/description/",
    "beats": 0.0,
    "category": ["stack and array"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 虽然temperatures很长，但是值域只有[30, 100]
	- 因此可以用这个值域来做buckets，每个temperature都可以遍历这个值域来找在它之后最近的较大点
	- 这个方法很笨，O(mn)
"""

class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        lst = []
        dct = {k:float('-inf') for k in range(30, 101)}
        for idx, temperature in enumerate(reversed(temperatures)):
            delta = float('inf')
            for t in range(temperature+1, 101):
                delta = min(idx - dct[t], delta)
            if delta > 30000:
                delta = 0
            lst.append(delta)
            dct[temperature] = idx
        return lst[::-1]
