"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/implement-queue-using-stacks/description/",
    "beats": 0.6582,
    "category": ["stack and array"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 用两个stack来模拟queue
	- push只在第一个stack中
	- pop先在第二个中取，如果没有，再把第一个stack中的所有元素倒过来填入stack2，再取
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack2) == 0:
            self.stack2 = self.stack1[::-1]
            self.stack1 = []
        return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack2) == 0:
            self.stack2 = self.stack1[::-1]
            self.stack1 = []
        return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()