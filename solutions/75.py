"""
{
	"author": "Yucheng Huang",
    "difficulty": "medium",
	"link": "https://leetcode.com/problems/sort-colors/description/",
	"category": ["sort"],
	"tags": ["partition","三向切分快速排序"]
}
"""

"""
荷兰国旗问题
	- 它其实是三向切分快速排序的一种变种，在三向切分快速排序中，每次切分都将数组分成三个区间：小于切分元素、等于切分元素、大于切分元素，而该算法是将数组分成三个区间：等于红色、等于白色、等于蓝色。
	
For more information, see https://www.cnblogs.com/ganganloveu/p/3703746.html
"""

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l,r = 0,len(nums)-1
        while r>0 and nums[r] == 2:
            r -= 1
        while l<=r and nums[l] == 0:
            l += 1
        i = l
        while i<=r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1
        