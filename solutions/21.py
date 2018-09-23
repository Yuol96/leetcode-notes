"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/merge-two-sorted-lists/description/",
    "beats": 0.9573,
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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l2.val < l1.val:
            p = l2
            l2 = l2.next
        else:
            p = l1
            l1 = l1.next
        head = p
        
        while l1 is not None and l2 is not None:
            if l2.val < l1.val:
                p.next = l2
                p = p.next
                l2 = l2.next
            else:
                p.next = l1
                p = p.next
                l1 = l1.next
        while l1 is not None:
            p.next = l1
            p = p.next
            l1 = l1.next
        while l2 is not None:
            p.next = l2
            p = p.next
            l2 = l2.next
            
        return head
