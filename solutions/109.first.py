"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/",
    "beats": 0.1808,
    "category": ["tree"],
    "tags": ["BST"],
    "questions": ["Is there any better method? `findPreMid` function seems to be a waste of time!"]
}
"""

"""
思路
	- 类似于108题，每次找到链表的mid，再递归构建BST
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findPreMid(self, head):
        slow, fast = head, head.next
        preMid = head
        while fast is not None and fast.next is not None:
            preMid = slow
            slow = slow.next
            fast = fast.next.next
        return preMid
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        preMid = self.findPreMid(head)
        mid = preMid.next
        preMid.next = None
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root
