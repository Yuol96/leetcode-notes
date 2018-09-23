"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/",
    "beats": 0.9979,
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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        p = head
        count = 1
        while p.next is not None:
            p = p.next
            count += 1
        if n==count:
            return head.next
        else:
            p = head
            idx = 1
            while idx != count-n:
                p = p.next
                idx += 1
            p.next = p.next.next
            return head
