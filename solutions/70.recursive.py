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
	- 为了避免重复计算，采用记忆性递归 --- 动态规划
"""

class Solution:
    
    def DP(self,n):
        if n in self.record:
            return self.record[n]
        ans = self.DP(n-1) + self.DP(n-2)
        self.record[n] = ans
        return ans
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.record = {
            0:1,
            1:1,
        }
        return self.DP(n)