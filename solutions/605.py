"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/can-place-flowers/description/",
    "category": ["greedy"],
    "tags": [],
    "questions": []
}
"""

"""
ATTENTION
	- 边界：flowerbed两侧要补0，`flowerbed = [0] + flowerbed + [0]`
"""

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        start, end = None, None
        flowerbed = [0] + flowerbed + [0]
        count = 0
        for idx,bed in enumerate(flowerbed):
            if bed == 0:
                if start is None:
                    start = idx
                else:
                    end = idx
            else :
                if start is not None and end is not None:
                    count += (end-start)//2
                start, end = None, None  
            # print(start, end, count)
        if start is not None and end is not None:
            count += (end-start)//2
        # print(count)
        return n<=count
