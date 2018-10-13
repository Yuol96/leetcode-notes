"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/find-the-duplicate-number/description/",
    "beats": 0.2290,
    "category": ["array"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- binary search by values (not by index)
	- please refer to `378.binary-search.py`
"""

class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)-1
        l,r = 1,n
        while l<r:
            midValue = (l+r)//2
            count = 0
            for num in nums:
                if num <= midValue:
                    count += 1
            if count > midValue:
                r = midValue
            # elif count < midValue:
            #     raise Exception
            else:
                l = midValue+1
        return l