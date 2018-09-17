"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/longest-increasing-subsequence/description/",
    "beats": 0.8133,
    "category": ["dynamic-programming"],
    "tags": ["subsequence"],
    "questions": []
}
"""

"""
思路：
	- 维护一个list，当下一个元素a比list最后一个元素大（说明满足递增条件），就append a；否则在list中找到(二分查找)恰好大于等于a的元素，代替它
"""

def replace(lst, item):
    """
    lst is an increasing array
    """
    l,r = 0,len(lst)
    while True:
        mid = l + (r-l)//2
        if lst[mid] > item:
            r = mid
        elif lst[mid] < item:
            l = mid + 1
        else :
            return
        if l==r:
            break
    lst[r] = item
            

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        lis = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > lis[-1]:
                lis.append(nums[i])
            elif nums[i] < lis[-1]:
                replace(lis, nums[i])
        return len(lis)
        
