"""
{
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/integer-break/description/",
    "category": ["dynamic-programming"],
    "tags": ["integer-break"],
    "questions": []
}
"""

"""
思路：
	- 递推公式：DP(n) = 对所有i in range(1,n)的 max(DP(n-i)*i, (n-i)*i)
		- 注意这里有个max是因为DP的题目要求是必须要拆分成两个数，因此DP(n-i)*i就至少是拆分成了三个数，还需要考虑两个数的情况
"""

class Solution:
    
    def DP(self, n):
        if n in self.record:
            return self.record[n]
        maxNum = 0
        for i in range(1, n):
            num = self.DP(n-i) * i
            num = max(num, (n-i)*i)
            if num > maxNum:
                maxNum = num
        self.record[n] = maxNum
        return maxNum
        
    
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.record = {
            1: 1,
            2: 1,
        }
        return self.DP(n)