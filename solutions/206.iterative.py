"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/intersection-of-two-linked-lists/description/",
    "beats": 0.7575,
    "category": ["linked-list"],
    "tags": [],
    "questions": []
}
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = None
        p = head
        while p is not None:
            tmp = newHead
            newHead = p
            p = p.next
            newHead.next = tmp
        return newHead
