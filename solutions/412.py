"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/fizz-buzz/description/",
    "beats": 0.1822,
    "category": ["Very Easy Questions"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lst = []
        for i in range(1,n+1):
            s = ""
            if i%3==0:
                s += "Fizz"
            if i%5==0:
                s += "Buzz"
            if s=="":
                s = str(i)
            lst.append(s)
        return lst