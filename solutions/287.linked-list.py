"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/find-the-duplicate-number/description/",
    "beats": 0.1579,
    "category": ["array"],
    "tags": ["linked list circle"],
    "questions": []
}
"""

"""
思路
	- 把nums看成链表，每个num是linkNode.next的地址
	- 有duplicate就意味着是有环链表
	- 通过two pointers法找环入口
	- please refer to https://leetcode.com/problems/find-the-duplicate-number/discuss/72846/My-easy-understood-solution-with-O(n)-time-and-O(1)-space-without-modifying-the-array.-With-clear-explanation.
"""

class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow