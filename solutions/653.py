"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/",
    "beats": 0.3082,
    "category": ["tree"],
    "tags": ["BST"],
    "questions": []
}
"""

"""
思路
	- 把BST转化为sorted array，再用two pointers法找target
	- 应该注意到，这一题不能用分别在左右子树两部分来处理这种思想，因为两个待求的节点可能分别在左右子树中。
"""

class Solution:
    def getSortedArray(self, root):
        if root is None:
            return
        self.getSortedArray(root.left)
        self.sortedArray.append(root.val)
        self.getSortedArray(root.right)
    
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.sortedArray = []
        self.getSortedArray(root)
        i,j = 0,len(self.sortedArray)-1
        while i<j:
            s = self.sortedArray[i]+self.sortedArray[j]
            if s > k:
                j -= 1
            elif s < k:
                i += 1
            else:
                return True
        return False