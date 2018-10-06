"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/palindrome-number/description/",
    "beats": 0.1355,
    "category": ["string"],
    "tags": ["palindrome"],
    "questions": []
}
"""

"""
思路
	- 不能使用extra space，也不能转化为str
	- 类似于two pointers
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        high = 1
        low = 1
        while x//high>=10:
            high *= 10
        while high > low:
            if (x//high)%10 != (x//low)%10:
                return False
            high //= 10
            low *= 10
        return True