"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/",
    "beats": 0.3179,
    "category": ["tree"],
    "tags": ["BST"],
    "questions": []
}
"""

"""
思路
	- 为了不使用extra space，需要遍历两次BST，第一次找到maxCount，第二次根据maxCount找到所有的modes
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def DFS(self, node, mode):
        if node is None:
            return
        self.DFS(node.left, mode)
        self.visit(node, mode)
        self.DFS(node.right, mode)
        
    def visit(self, node, mode):
        if mode == 0:
            if self.preNode is None:
                self.preNode = node
                self.count = 1
            else :
                if self.preNode.val == node.val:
                    self.count += 1
                else :
                    self.maxCount = max(self.maxCount, self.count)
                    self.preNode = node
                    self.count = 1
        elif mode == 1:
            if self.preNode is None:
                self.preNode = node
                self.count = 1
            else :
                if self.preNode.val == node.val:
                    self.count += 1
                else :
                    if self.count == self.maxCount:
                        self.nums.append(self.preNode.val)
                    self.preNode = node
                    self.count = 1
    
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        self.preNode = None
        self.maxCount = 0
        self.count = 0
        self.DFS(root, 0)
        self.maxCount = max(self.maxCount, self.count)
        # print(self.maxCount)
        
        self.preNode = None
        self.nums = []
        self.DFS(root, 1)
        if self.count == self.maxCount:
            self.nums.append(self.preNode.val)
        return self.nums