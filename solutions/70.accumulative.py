"""
{
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/climbing-stairs/description/",
    "category": ["dynamic-programming"],
    "tags": ["fibonacci"],
    "questions": []
}
"""

"""
思路：
	- 考虑递推公式，DP(i) = DP(i-1) + DP(i-2)
	- 从小到大依次计算
"""

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        a = 1
        b = 2
        for i in range(2, n):
            tmp = a+b
            a = b
            b = tmp
        return b