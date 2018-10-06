"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/min-stack/description/",
    "beats": 0.4004,
    "category": ["stack and array"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 空间换时间，多用一个minstack来保持每一步的最小值
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.datastack = []
        self.minstack = [float('inf')]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.datastack.append(x)
        self.minstack.append(min(self.minstack[-1], x))

    def pop(self):
        """
        :rtype: void
        """
        self.datastack.pop()
        self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.datastack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()