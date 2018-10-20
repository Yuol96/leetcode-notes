"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/count-and-say/description/",
    "beats": 0.3271,
    "category": ["string"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        lastSeq = self.countAndSay(n-1)
        lastChar = lastSeq[0]
        idx = 1
        count = 1
        s = ""
        while idx < len(lastSeq):
            if lastChar == lastSeq[idx]:
                count += 1
            else :
                s += "{}{}".format(count,lastChar)
                count = 1
                lastChar = lastSeq[idx]
            idx += 1
        s += "{}{}".format(count,lastChar)
        return s