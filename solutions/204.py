"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/count-primes/description/",
    "beats": 0.1920,
    "category": ["math"],
    "tags": ["prime"],
    "questions": []
}
"""

"""
思路：
	- 每iterate一个数，就把他之后的倍数都去掉
"""

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0
        lst = [1 for __ in range(n)]
        lst[0] = 0
        lst[1] = 0
        idx = 2
        while idx < n:
            if lst[idx]:
                for i in range(idx+idx, n, idx):
                    lst[i] = 0
            idx += 1
        return sum(lst)