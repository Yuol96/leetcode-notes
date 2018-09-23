"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/intersection-of-two-linked-lists/description/",
    "beats": 0.3977,
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
    def recursive(self, node):
        if node.next is None:
            return node, node
        newHead, parentNode = self.recursive(node.next)
        parentNode.next = node
        return newHead, node
            
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        newHead, tailNode = self.recursive(head)
        tailNode.next = None
        return newHead
