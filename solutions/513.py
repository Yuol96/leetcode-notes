"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/find-bottom-left-tree-value/description/",
    "beats": 0.0826,
    "category": ["tree"],
    "tags": ["BFS"],
    "questions": []
}
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = Queue()
        q.put(root)
        while not q.empty():
            num = q.qsize()
            for idx in range(num):
                node = q.get()
                if idx == 0:
                    leftMost = node.val
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
        return leftMost