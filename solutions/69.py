"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/sqrtx/description/",
    "category": ["binary-search"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l,r = 1,x
        while True:
            mid = l + (r-l)//2
            if mid**2 > x:
                r = mid
            elif mid**2 < x:
                l = mid
            else :
                return mid
            # print(l,r)
            if l == r-1:
                break
            
        if r**2 > x:
            return l
        else:
            return r