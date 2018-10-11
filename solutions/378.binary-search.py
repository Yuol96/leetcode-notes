"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/",
    "beats": 0.1220,
    "category": ["array"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- binary search based on values (not index)
"""

class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        l,r = matrix[0][0],matrix[n-1][n-1]
        while l<r:
            mid = (l+r)//2
            count = 0
            for i in range(n):
                for j in range(n):
                    if matrix[i][j]>mid:
                        break
                    count += 1
            # print(l,r,mid,count)
            if count < k:
                l = mid+1
            else:
                r = mid
        return l
