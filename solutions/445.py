"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/add-two-numbers-ii/description/",
    "beats": 49.74,
    "category": ["linked-list"],
    "tags": [],
    "questions": []
}
"""

"""
- 另一种思路是用栈来存储linked list里面的元素，再反向生成
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def linkedList2num(self, l):
        v = 0
        while l is not None:
            v *= 10
            v += l.val
            l = l.next
        return v
    
    def num2linkedList(self, num):
        s = str(num)
        head = ListNode(None)
        p = head
        for c in s:
            p.next = ListNode(int(c))
            p = p.next
        return head.next
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = self.linkedList2num(l1)
        b = self.linkedList2num(l2)
        return self.num2linkedList(a+b)