"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/intersection-of-two-arrays-ii/description/",
    "beats": 0.6826,
    "category": ["array"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        i,j = 0,0
        lst = []
        while i<len(nums1) and j<len(nums2):
            a,b = nums1[i],nums2[j]
            if a>b:
                j+=1
            elif a<b:
                i+=1
            else:
                lst.append(a)
                i+=1
                j+=1
        return lst