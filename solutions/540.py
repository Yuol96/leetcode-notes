"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/single-element-in-a-sorted-array/description/",
    "category": ["binary-search"],
    "tags": [],
    "questions": []
}
"""

"""
思路：
	- mid要分奇数和偶数两种情况讨论
"""


class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0,len(nums)-1
        while True:
            mid = l+(r-l)//2
            if mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    l = mid + 1
                else:
                    r = mid
            elif mid % 2 == 1:
                if nums[mid] != nums[mid+1]:
                    l = mid + 1
                else:
                    r = mid - 1
            # print(l,r)
            if l==r:
                break
        return nums[l]
