"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/",
    "category": ["binary-search"],
    "tags": [],
    "questions": []
}
"""

"""
ATTENTION
	- binarySearch一定要考虑待查元素在array之外的情况！！！
	- array只有一个元素时，使用`if l>=r-1` 作为break条件才不会出bug
"""

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] < nums[-1]:
            return nums[0]
        l,r = 0,len(nums)-1
        while True:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid
            else :
                r = mid
            # print(l,r)
            if l >= r-1:
                break
        return nums[r]
                