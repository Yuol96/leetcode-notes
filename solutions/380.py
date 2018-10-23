"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/insert-delete-getrandom-o1/",
    "beats": 0.9877,
    "category": ["hash table"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 为了去除list中间的某个元素而不引起后续元素index的改变，可以用list中最后一个元素来填补空缺
"""

import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.num2idx = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.num2idx:
            return False
        self.num2idx[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.num2idx:
            return False
        idx = self.num2idx.pop(val)
        if idx == len(self.nums)-1:
            self.nums.pop(-1)
        else:
            lastNum = self.nums.pop(-1)
            self.nums[idx] = lastNum
            self.num2idx[lastNum] = idx
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()