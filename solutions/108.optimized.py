"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/",
    "beats": 0.4718,
    "category": ["tree"],
    "tags": ["BST"],
    "questions": []
}
"""

"""
思路
	- avoid deep copy `nums`
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def DFS(self, i, j):
        if i==j:
            return None
        mid = (j+i-1)//2
        root = TreeNode(self.nums[mid])
        root.left = self.DFS(i, mid)
        root.right = self.DFS(mid+1, j)
        return root
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.nums = nums
        return self.DFS(0, len(nums))