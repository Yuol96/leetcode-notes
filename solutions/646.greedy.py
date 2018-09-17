"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/maximum-length-of-pair-chain/description/",
    "beats": 0.9760,
    "category": ["dynamic-programming", "greedy"],
    "tags": ["overlapping-intervals"],
    "questions": []
}
"""

"""
思路：
	- greedy：按照pair[1]从小到大排序（防止overlap），逐个iterate，去除overlapping intervals
"""

class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if not pairs:
            return 0
        pairs.sort(key=lambda pair: pair[1])
        ret = 1
        lastPair = pairs[0]
        for idx in range(1, len(pairs)):
            pair = pairs[idx]
            if pair[0] > lastPair[1]:
                lastPair = pair
                ret += 1
        return ret


