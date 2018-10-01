"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/binary-tree-preorder-traversal/description/",
    "beats": 0.4299,
    "category": ["tree"],
    "tags": ["DFS","traversal"],
    "questions": []
}
"""

class Solution:
    def __init__(self):
        self.lst = []
        
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        self.lst.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.lst