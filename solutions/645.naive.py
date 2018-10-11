"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/set-mismatch/description/",
    "beats": 0.6412,
    "category": ["array"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)        
        st = set()
        for num in nums:
            if num in st:
                duplicate = num
            else:
                st.add(num)
        for i in range(1,n+1):
            if i not in st:
                missing = i
                return [duplicate, missing]