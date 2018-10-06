"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/reshape-the-matrix/description/",
    "beats": 0.9787,
    "category": ["array"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        num_rows = len(nums)
        num_cols = len(nums[0])
        if num_rows*num_cols != r*c:
            return nums
        
        new_row = []
        new_nums = []
        counts = 0
        for row in nums:
            for ele in row:
                new_row.append(ele)
                counts += 1
                if counts==c:
                    new_nums.append(new_row)
                    new_row = []
                    counts = 0
                    
        return new_nums