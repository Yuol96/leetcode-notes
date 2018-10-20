"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/hamming-distance/description/",
    "beats": 0.3946,
    "category": ["bit manipulation"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 用n&(n-1)去除n的最低位
"""

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        tmp = x^y
        count = 0
        while tmp>0:
            tmp &= (tmp-1)
            count += 1
        return count