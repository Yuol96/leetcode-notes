"""
{
	"author": "Yucheng Huang",
    "difficulty": "medium",
	"link": "https://leetcode.com/problems/assign-cookies/description/",
	"category": ["greedy"],
	"tags": ["binary-search"]
}
"""

def binarySearch(item,s):
    if item > s[-1]:
        return None
    i,j =  0,len(s)-1
    while i<=j:
        if s[i] >= item:
            return i, s[i]
        mid = (i+j)//2
        if s[mid]>=item:
            j = mid
        elif s[mid]<item:
            i = mid+1
            
class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        s.sort()
        g.sort()
        count = 0
        for childG in g:
            if s:
                tup = binarySearch(childG, s)
                if tup:
                    cookieIdx, cookieSize = tup
                    assert cookieSize >= childG, (cookieSize, childG)
                    count += 1
                    s.pop(cookieIdx)
                else:
                    break
            else :
                break
        return count
            
