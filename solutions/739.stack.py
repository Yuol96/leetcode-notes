"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/daily-temperatures/description/",
    "beats": 0.2526,
    "category": ["stack and array"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 遍历数组，逐个放入stack中
	- 如果当前遍历到的temperature比栈顶的元素大，那么说明它的最近的较大点就是当前遍历的元素
"""

class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        lst = [0 for __ in range(len(temperatures))]
        stack = []
        for idx, t in enumerate(temperatures):
            while len(stack)>0 and temperatures[stack[-1]]<t:
                lst[stack[-1]] = idx - stack[-1]
                stack.pop()
            stack.append(idx)
        return lst
