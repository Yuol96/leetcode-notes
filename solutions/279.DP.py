"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/perfect-squares/description/",
    "category": ["BFS","dynamic-programming"],
    "tags": ["integer-break"],
    "questions": ["Why the commented version becomes TLE while the two version seems to be the same"]
}
"""

"""
思路：
	- 递推公式：DP(n) = min([DP(n-square) for square in 所有小于等于n的完全平方数]) + 1
"""

# class Solution:
#     def numSquares(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         record = [0]
#         for i in range(1, n+1):
#             record.append(min([record[-j*j] for j in range(1,int(i**0.5)+1)]) + 1)
#         return record[n]
    
class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]