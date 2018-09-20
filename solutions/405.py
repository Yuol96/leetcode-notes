"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/",
    "beats": 0.4479,
    "category": ["math"],
    "tags": ["base-conversion"],
    "questions": []
}
"""

"""
思路：
	- 十六进制可以利用基于二进制的bit manipulation
"""

class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        fourBitMask = 15
        lst = list('0123456789abcdef')
        ans = []
        for idx in range(8):
            ans.append(lst[num & fourBitMask])
            num >>= 4
        ans = ''.join(reversed(ans))
        start = 0
        while start < 8 and ans[start]=="0":
            start += 1
        return ans[start:]