"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/average-of-levels-in-binary-tree/description/",
    "beats": 0.0789,
    "category": ["tree"],
    "tags": ["BFS"],
    "questions": []
}
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root is None:
            return []
        q = Queue()
        q.put(root)
        ans = []
        while not q.empty():
            num = q.qsize()
            lst = []
            for __ in range(num):
                node = q.get()
                lst.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            ans.append(sum(lst)/len(lst))
        return ans