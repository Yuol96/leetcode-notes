"""
{
	"difficulty": "medium",
	"link": "https://leetcode.com/problems/top-k-frequent-elements/description/",
	"category": ["sort"],
	"tags": ["topk","bucket-sort"]
}
"""

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dct = {}
        for num in nums:
            dct[num] = dct.get(num,0) + 1
        lst = sorted(list(dct.items()), key=lambda tup: tup[1], reverse=True)[:k]
        return list(map(lambda tup: tup[0], lst))