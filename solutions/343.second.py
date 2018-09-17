"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/integer-break/description/",
    "category": ["dynamic-programming"],
    "tags": ["integer-break"],
    "questions": []
}
"""

"""
思路：
	- 递推公式：DP(n) = 对所有i in range(1,n)的 max(DP(n-i)*i, n)
	- 注意second版本和first版本的区别是，这里的DP不要求n分成至少两个数
"""

class Solution:
    def DP(self, n):
        if n in self.record:
            return self.record[n]
        maxNum = 0
        for i in range(1,n):
            maxNum = max(self.DP(n-i)*i, maxNum)
        maxNum = max(n, maxNum)
        self.record[n] = maxNum
        return maxNum
    
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.record = {
            1: 1,
        }
        ret = 0
        for i in range(1, n):
            ret = max(ret, self.DP(n-i)*i)
        return ret