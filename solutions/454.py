"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/4sum-ii/description/",
    "beats": 0.2983,
    "category": ["hash table"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 4个list，两两一组，分别计算其和的dict，再合并
"""

class Solution:
    def twoSumDict(self, A, B):
        dct = {}
        for a in A:
            for b in B:
                val = a+b
                dct[val] = dct.get(val,0) + 1
        return dct
    
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dct1 = self.twoSumDict(A,B)
        dct2 = self.twoSumDict(C,D)
        count = 0
        for num in dct1:
            if -num in dct2:
                count += dct1[num]*dct2[-num]
        return count