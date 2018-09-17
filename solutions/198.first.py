"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/house-robber/description/",
    "category": ["dynamic-programming"],
    "tags": ["fibonacci"],
    "questions": []
}
"""

class Solution:
    '''
    思路： 
        动态规划，假设最后偷的的房子的下标为idx（从0开始）的最大收益为robber(idx)，则有
        robber(idx) = max( robber(idx-1),
                           robber(idx-2) + nums[idx],
                           robber(idx-3) + nums[idx])
       注意，robber(idx-3) + nums[idx]是必须考虑在内的！
    '''
    def __init__(self):
        self.record = {}
        self.nums = []
        
    def robber(self, idx):
#         print(idx)
        if self.record.get(idx,None) is None:
            if idx<=1:
                self.record[idx] = self.nums[idx]
                return self.record[idx]
            lst = []
            lst.append(self.robber(idx-2) + self.nums[idx])
            lst.append(self.robber(idx-1))
            if idx>2:
                lst.append(self.robber(idx-3) + self.nums[idx])
            
            self.record[idx] = max(lst)
            
            return self.record[idx]
            
        else :
            return self.record[idx]
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        L = len(nums)
        if L==0:
            return 0  
        
        return max(self.robber(len(nums)-1),self.robber(len(nums)-2))