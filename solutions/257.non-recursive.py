"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/binary-tree-paths/description/",
    "category": ["DFS"],
    "tags": ["backtracking","binary-tree"],
    "questions": []
}
"""

"""
思路：
	- 非递归，手动模拟递归栈的过程。path存储每条递归链的数值，stack存储每次递归的状态
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root:
            stack = [(root, 0)]
            path = []
            lst = []
            while stack:
                node, height = stack.pop()
                path.append(str(node.val))
                if node.left:
                    stack.append((node.left, height+1))
                if node.right:
                    stack.append((node.right, height+1))
                if not node.left and not node.right:
                    lst.append('->'.join(path))
                    while stack and stack[-1][1] < len(path):
                        path.pop()
            return lst
                    
        else :
            return []
