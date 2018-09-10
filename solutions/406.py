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
按k值升序，h降序，依次插入
"""

class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if people:
            dct = {}
            for p in people:
                dct[p[1]] = dct.get(p[1],[]) + [p]

            for k in dct:
                dct[k].sort(key=lambda p:p[0],reverse=True)

            lst = sorted(dct[0].copy(), key=lambda p:p[0])
            dct.pop(0)

            currk = 1
            for currk in sorted(list(dct.keys())):
                plist = dct[currk]
                for p in plist:
                    count = 0
                    for idx,existp in enumerate(lst):
                        if existp[0]>= p[0]:
                            count += 1
                        if count == currk:
                            lst = lst[:idx+1] + [p] + lst[idx+1:]
                            break
            return lst
        else :
            return []
        
        
