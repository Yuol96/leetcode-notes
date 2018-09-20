"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/excel-sheet-column-title/description/",
    "beats": 0.0397,
    "category": ["math"],
    "tags": ["base-conversion"],
    "questions": []
}
"""

"""
思路
	- 由于每轮A-Z都会多一个，所以while循环中需要有n-=1
"""

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        mapping = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        ans = []
        base = 26
        while n>0:
            n -= 1
            ans.append(n%base)
            n //= base
        print(ans)
        return ''.join(map(lambda num: mapping[num], reversed(ans)))

