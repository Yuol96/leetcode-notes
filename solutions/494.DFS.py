"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/target-sum/description/",
    "beats": 0,
    "category": ["dynamic-programming","DFS"],
    "tags": ["knapsack"],
    "questions": []
}
"""

class Solution:
    def DFS(self, currState, idx):
        # print(nums)
        if self.L == idx:
            if currState == self.S:
                self.count += 1
            return
        
        num = self.nums[idx]
        self.DFS(currState+num, idx+1)
        self.DFS(currState-num, idx+1)
    
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.count = 0
        self.nums = nums
        self.L = len(nums)
        self.S = S
        self.DFS(0, 0)
        return self.count