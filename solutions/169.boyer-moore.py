"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/majority-element/description/",
    "beats": 0.4223,
    "category": ["math"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 利用 Boyer-Moore Majority Vote Algorithm
	- 使用 cnt 来统计一个元素出现的次数，当遍历到的元素和统计元素不相等时，令 cnt--。如果前面查找了 i 个元素，且 cnt == 0，说明前 i 个元素没有 majority，或者有 majority，但是出现的次数少于 i / 2，因为如果多于 i / 2 的话 cnt 就一定不会为 0。此时剩下的 n - i 个元素中，majority 的数目依然多于 (n - i) / 2，因此继续查找就能找出 majority。
"""

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = nums[0]
        L = len(nums)
        count = 1
        if L>1:
            for i in range(1, L):
                if nums[i] == num:
                    count += 1
                else :
                    count -= 1
                    if count < 0:
                        num = nums[i]
                        count = 1
        return num