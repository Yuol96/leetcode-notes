"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/map-sum-pairs/description/",
    "beats": 0.4069,
    "category": ["tree"],
    "tags": ["trie"],
    "questions": []
}
"""

"""
思路
	- please refer to `208.dict-optimized.py`
"""

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        
    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        dct = self.root
        for c in key:
            if c not in dct:
                dct[c] = {}
            dct = dct[c]
        dct['val'] = val

    def getSum(self, dct):
        ret = dct.get('val', 0)
        for c,child_dct in dct.items():
            if c != 'val':
                ret += self.getSum(child_dct)
        return ret
        
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        dct = self.root
        for c in prefix:
            if c not in dct:
                return 0
            dct = dct[c]
        return self.getSum(dct)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)