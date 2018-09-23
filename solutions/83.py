"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/",
    "beats": 0.5069,
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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        p = head
        while True:
            if p.next is None:
                break
            if p.next.val == p.val:
                p.next = p.next.next
            else :
                p = p.next
        return head