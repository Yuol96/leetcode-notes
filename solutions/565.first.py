"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/array-nesting/",
    "beats": 0.8724,
    "category": ["array"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- two pointers法求有环链表的环的长度
	- 这里可能有多个有环链表，而不是单一链表
"""

class Solution:
    def getCycleLen(self, nums, visited, idx):
        if len(nums)<2:
            return 1
        slow = nums[idx]
        fast = nums[nums[idx]]
        visited[idx] = 1
        visited[nums[idx]] = 1
        count = 1
        while slow != fast:
            slow = nums[slow]
            visited[slow] = 1
            fast = nums[nums[fast]]
            visited[fast] = 1
            visited[nums[fast]] = 1
            count += 1
        return count
    
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = [0 for __ in range(len(nums))]
        maxCount = 0
        for i in range(len(nums)):
            if visited[i]==0:
                count = self.getCycleLen(nums, visited, i)
                maxCount = max(maxCount, count)
        return maxCount
