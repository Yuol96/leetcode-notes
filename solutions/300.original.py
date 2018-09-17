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

def lower_bound(lst, query):
    if query < lst[0]:
        return 0
    if query > lst[-1]:
        return len(lst)
    L = len(lst)
    left = 0
    right = L - 1
    while left<=right:
        mid = int((left + right)//2)
        if lst[mid]< query:
            left = mid
        elif lst[mid] > query:
            right = mid
        else :
            return mid
        if left + 1 == right:
            if query == lst[left]:
                return left
            else:
                return right

class Solution:
    def __init__(self):
        self.lst = []
    
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        self.lst.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i] <= self.lst[-1]:
                idx = lower_bound(self.lst, nums[i])
                self.lst[idx] = nums[i]
            else :
                self.lst.append(nums[i])
        return len(self.lst)
        