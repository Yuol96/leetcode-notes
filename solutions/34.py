"""
{
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/",
    "category": ["binary-search"],
    "tags": [],
    "questions": []
}
"""

"""
ATTENTION
	- 在findLarge里面最后两个if的顺序和findSmall里面是相反的！！！
"""

def findSmall(nums, target):
    if target < nums[0] or target > nums[-1]:
        return -1
    l,r = 0,len(nums)-1
    while True:
        mid = l + (r-l)//2
        if nums[mid]>=target:
            r = mid
        else :
            l = mid
        if l >= r - 1:
            break
    if nums[l] == target:
        return l
    if nums[r] == target:
        return r
    return -1

def findLarge(nums, target):
    if target < nums[0] or target > nums[-1]:
        return -1
    l,r = 0,len(nums)-1
    while True:
        mid = l + (r-l)//2
        if nums[mid]<=target:
            l = mid
        else :
            r = mid
        print(l,r)
        if l >= r - 1:
            break
    if nums[r] == target:
        return r
    if nums[l] == target:
        return l
    return -1
    

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums:
            i = findSmall(nums, target)
            j = findLarge(nums, target)
            return i,j
        return [-1,-1]
