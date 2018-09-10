"""
{
	"difficulty": "medium",
	"link": "https://leetcode.com/problems/queue-reconstruction-by-height/description/",
	"category": ["greedy"],
	"tags": [],
	"questions": []
}
"""

"""
思路：
	- 反过来，先h降序，再按k值升序，依次插入。这样的好处是每次插入不需要检查，插入的people.k就是index。
	- `list.sort(key=lambda p: (-p[0], p[1]))`
	- `list.insert(index, obj)`
"""

class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda p: (-p[0], p[1]))
        lst = []
        for p in people:
            lst.insert(p[1],p)
        return lst