"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/delete-node-in-a-linked-list/description/",
    "beats": 0.9162,
    "category": ["Very Easy Questions"],
    "tags": [],
    "questions": []
}
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        nextNode = node.next
        node.val = nextNode.val
        node.next = nextNode.next