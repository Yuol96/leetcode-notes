"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/longest-univalue-path/description/",
    "beats": 0.9278,
    "category": ["tree"],
    "tags": ["DFS"],
    "questions": []
}
"""

"""
ATTENTION
    - 递归时，对每个递归的结点都需要有self.maxLen = max(self.maxLen, currLen)
    - 但是每次递归的返回值却只能是左子树和右子树中最长的那一条+1，而不能把二者相加
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def DFS(self, node):
        if node is None:
            return 0
        currLen = 0
        ret = 0
        a, b = self.DFS(node.left), self.DFS(node.right)
        if node.left and node.left.val == node.val:
            currLen += a + 1
            ret = a+1
        if node.right and node.right.val == node.val:
            currLen += b + 1
            ret = max(ret, b+1)
        self.maxLen = max(self.maxLen, currLen)
        # print(node.val, currLen)
        return ret
    
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.maxLen = 0
        self.DFS(root)
        return self.maxLen


