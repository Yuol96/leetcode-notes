"""
{
	"author": "Yucheng Huang",
    "difficulty": "easy",
	"link": "https://leetcode.com/problems/sum-of-square-numbers/description/",
	"category": ["two pointers"],
    "tags": []
}
"""
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i, j = 0, int(c**0.5)
        flag = False
        while i<=j:
            tmp = i**2 + j**2
            if tmp < c:
                i += 1
            elif tmp > c:
                j -= 1
            else :
                flag = True
                break
        return flag