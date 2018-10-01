"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/binary-tree-preorder-traversal/description/",
    "beats": 0.1437,
    "category": ["tree"],
    "tags": ["DFS","traversal"],
    "questions": []
}
"""

"""
思路：
	- 用direction来指示递归返回的方向，如果direction==0，需要说明左子树还未递归，如果direction==1，则说明该递归右子树了
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        lst = []
        stack.append((root, 0))
        while len(stack)>0:
            node, direction = stack.pop()
            if node is not None:
                if direction == 0:
                    lst.append(node.val)
                    stack.append((node, 1))
                    stack.append((node.left, 0))
                elif direction == 1:
                    stack.append((node.right, 0))
                    
        return lst