"""
{
	"difficulty": "medium",
	"link": "https://leetcode.com/problems/sort-characters-by-frequency/description/",
	"category": ["sort"],
	"tags": ["bucket-sort"]
}
"""

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dct = {}
        for c in s:
            dct[c] = dct.get(c, 0) + 1
        output = ""
        for c,count in sorted(list(dct.items()), key=lambda tup: tup[1], reverse=True):
            output += c*count
        return output