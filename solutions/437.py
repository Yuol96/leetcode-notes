"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/path-sum-iii/description/",
    "beats": 0.5531,
    "category": ["tree"],
    "tags": ["DFS"],
    "questions": []
}
"""

"""
思路
	- 递归每一个结点，返回以这个结点为起点的所有可能长度的path的list
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
            return []
        lst = self.DFS(node.left) + self.DFS(node.right)
        for idx in range(len(lst)):
            lst[idx] += node.val
            if lst[idx] == self.sum:
                self.count += 1
        lst.append(node.val)
        if node.val == self.sum:
            self.count += 1
        return lst
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count = 0
        self.sum = sum
        self.DFS(root)
        return self.count