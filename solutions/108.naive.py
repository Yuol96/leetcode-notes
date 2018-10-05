"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/",
    "beats": 0.3461,
    "category": ["tree"],
    "tags": ["BST"],
    "questions": []
}
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        L = len(nums)
        if L == 0:
            return None
        if L == 1:
            return TreeNode(nums[0])
        mid = (L-1)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root