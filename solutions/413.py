"""
{
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/arithmetic-slices/description/",
    "category": ["dynamic-programming"],
    "tags": ["subarray"],
    "questions": []
}
"""

"""
思路：
	- 考虑以第i个元素结尾的arithmetic subarray的数目
"""

class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        self.L = len(A)
        if self.L < 3:
            return 0
        self.count = [0 for __ in range(self.L)]
        for i in range(2, len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                self.count[i] = self.count[i-1] + 1
            else :
                self.count[i] = 0
        return sum(self.count)
