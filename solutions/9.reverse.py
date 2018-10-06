"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/palindrome-number/description/",
    "beats": 0.0935,
    "category": ["string"],
    "tags": ["palindrome"],
    "questions": []
}
"""

"""
思路
	- 反向构造palindrome，再对比
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        reverse = 0
        tmp = x
        while x > 0:
            reverse = reverse * 10 + x%10
            x //= 10
        return reverse == tmp