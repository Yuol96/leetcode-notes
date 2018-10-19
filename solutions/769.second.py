"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/max-chunks-to-make-sorted/description/",
    "beats": 0.3923,
    "category": ["array"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 如果arr[:i+1]中的最大值就是i，那么count+=1
"""

class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        currMax = -1
        count = 0
        for idx in range(len(arr)):
            currMax = max(currMax, arr[idx])
            if currMax == idx:
                count += 1
        return count