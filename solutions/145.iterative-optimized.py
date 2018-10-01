"""
{
    "author": "Yucheng Huang",
    "difficulty": "hard",
    "link": "https://leetcode.com/problems/binary-tree-postorder-traversal/description/",
    "beats": 0.1096,
    "category": ["tree"],
    "tags": ["DFS","traversal"],
    "questions": []
}
"""

"""
思路：
	- 后序：left->right->root
	- 其逆向结果为：root->right->left，可以通过修改非递归前序遍历的代码得到。这样可以避免记录递归方向
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [root]
        lst = []
        while len(stack)>0:
            node = stack.pop()
            if node is None:
                continue
            lst.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
        return list(reversed(lst))