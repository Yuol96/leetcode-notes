"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/factorial-trailing-zeroes/description/",
    "beats": 0.3740,
    "category": ["math"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- N//5 + N//5^2 + N//5^3 + ...
	- 如果统计的是 N! 的二进制表示中最低位 1 的位置，只要统计有多少个 2 即可。和求解有多少个 5 一样，2 的个数为 N/2 + N/2^2 + N/2^3 + ...
"""

class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = n // 5
        count = 0
        while num > 0:
            count += num
            num //= 5
        return count