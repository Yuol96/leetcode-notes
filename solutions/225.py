"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/implement-stack-using-queues/description/",
    "beats": 0.0,
    "category": ["stack and array"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 在将一个元素 x 插入队列时，为了维护原来的后进先出顺序，需要让 x 插入队列首部。而队列的默认插入顺序是队列尾部，因此在将 x 插入队列尾部之后，需要让除了 x 之外的所有元素出队列，再入队列。
"""

from queue import Queue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q.put(x)
        
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        num = self.q.qsize()
        while num>1:
            self.q.put(self.q.get())
            num -= 1
        return self.q.get()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        num = self.q.qsize()
        while num>1:
            self.q.put(self.q.get())
            num -= 1
        tmp = self.q.get()
        self.q.put(tmp)
        return tmp

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q.qsize()==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()