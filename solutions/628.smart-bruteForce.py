"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/maximum-product-of-three-numbers/description/",
    "beats": 0.5960,
    "category": ["math"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 最大的三个正数or有两个最小负数
"""

class Solution:
    
    def bruteForce(self, nums):
        maxMul = float('-inf')
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    tmp = nums[i]*nums[j]*nums[k]
                    if tmp > maxMul:
                        maxMul = tmp
        return maxMul
    
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a = self.bruteForce(nums[-3:])
        b = self.bruteForce(nums[:2]+nums[-1:])
        return max(a,b)
            
                
