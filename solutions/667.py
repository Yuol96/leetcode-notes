"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/beautiful-arrangement-ii/description/",
    "beats": 0.2803,
    "category": ["array"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- [1,5,2,4,3], n=5, k=4
	- [1,5,4,3,2], n=5, k=2
	- [1,5,2,3,4], n=5, k=3
"""

class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        lst = [1]
        l,r = 2,n
        k -= 1
        while k>0:
            lst.append(r)
            r -= 1
            k -= 1
            if k<= 0:
                break
            lst.append(l)
            l += 1
            k -= 1
        if lst[-1]>r:
            while len(lst)<n:
                lst.append(r)
                r -= 1
        else:
            while len(lst)<n:
                lst.append(l)
                l += 1
        return lst