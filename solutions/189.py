"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/rotate-array/description/",
    "beats": 0.7018,
    "category": ["array"],
    "tags": ["in-place","**"],
    "questions": []
}
"""

"""
思路
	- 这是不同于`645.smart.py`的另一种思路
	- 把两段nums分别逆序，再整个逆序
"""

class Solution:
    def reverse(self, nums, i, j):
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1
    
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        L = len(nums)
        k = k%L
        self.reverse(nums,0,L-k-1)
        self.reverse(nums,L-k,L-1)
        self.reverse(nums,0,L-1)