"""
{
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/binary-tree-paths/description/",
    "category": ["DFS"],
    "tags": ["backtracking","binary-tree"],
    "questions": []
}
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def DFS(node, currPath, st):
    assert len(currPath) != 0
    assert node
    currPath += "->{}".format(node.val)
    
    if not node.left and not node.right:
        st.add(currPath)
        return
    
    if node.left:
        DFS(node.left, currPath, st)
    if node.right:
        DFS(node.right, currPath, st)

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        currPath = "{}".format(root.val)
        st = set()
        if not root.left and not root.right:
            st.add(currPath)
        if root.left:
            DFS(root.left, currPath, st)
        if root.right:
            DFS(root.right, currPath, st)
        return list(st)

        